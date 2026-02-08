import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("USDA_API_KEY")
BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

INPUT = "data/argenfood_limpio.csv"
OUTPUT = "data/argenfood_con_porciones.csv"
CACHE_FILE = "data/usda_cache.csv"

def obtener_porcion_usda(nombre):
    params = {
        "query": nombre,
        "pageSize": 1,
        "api_key": API_KEY
    }

    r = requests.get(BASE_URL, params=params, timeout=10)
    if r.status_code != 200:
        return None, None

    foods = r.json().get("foods", [])
    if not foods:
        return None, None

    for portion in foods[0].get("foodPortions", []):
        if portion.get("gramWeight"):
            return portion["gramWeight"], "USDA"

    return None, None

# =========================
# Cargar datos
# =========================
df = pd.read_csv(INPUT)

# Cargar cache si existe
if os.path.exists(CACHE_FILE):
    cache = pd.read_csv(CACHE_FILE)
else:
    cache = pd.DataFrame(columns=["alimento", "porcion_g", "fuente"])

cache_dict = dict(zip(cache["alimento"], zip(cache["porcion_g"], cache["fuente"])))

porciones = []
fuentes = []

total = len(df)

for i, alimento in enumerate(df["alimento"], start=1):
    if alimento in cache_dict:
        porcion, fuente = cache_dict[alimento]
    else:
        porcion, fuente = obtener_porcion_usda(alimento)
        time.sleep(0.3)

        if porcion is None:
            porcion = 50
            fuente = "RIGA"

        cache = pd.concat([
            cache,
            pd.DataFrame([{
                "alimento": alimento,
                "porcion_g": porcion,
                "fuente": fuente
            }])
        ], ignore_index=True)

        cache_dict[alimento] = (porcion, fuente)

    porciones.append(porcion)
    fuentes.append(fuente)

    print(f"[{i}/{total}] {alimento} → {porcion} g ({fuente})")

# Guardar resultados
df["porcion_g"] = porciones
df["fuente_porcion"] = fuentes

df.to_csv(OUTPUT, index=False)
cache.to_csv(CACHE_FILE, index=False)

print("✅ Porciones integradas con cache USDA")

