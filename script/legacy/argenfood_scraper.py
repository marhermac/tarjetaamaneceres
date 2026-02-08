import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.argenfood.unlu.edu.ar/Tablas/Tabla/"

CODIGOS = range(1, 500)  # ajustable
rows = []

for codigo in CODIGOS:
    url = f"{BASE_URL}{codigo}"
    r = requests.get(url, timeout=10)

    if r.status_code != 200:
        continue

    soup = BeautifulSoup(r.text, "html.parser")

    # 🟢 Nombre del alimento (clave)
    h1 = soup.find("h1")
    if not h1:
        continue

    alimento = h1.get_text(strip=True)

    # Tabla nutricional
    tabla = soup.find("table")
    if not tabla:
        continue

    data = {}
    for fila in tabla.find_all("tr"):
        cols = fila.find_all("td")
        if len(cols) != 2:
            continue
        clave = cols[0].get_text(strip=True).lower()
        valor = cols[1].get_text(strip=True).replace(",", ".")
        data[clave] = valor

    try:
        rows.append({
            "codigo": codigo,
            "alimento": alimento,
            "energia_kcal": data.get("energía (kcal)", ""),
            "carbohidratos_g": data.get("hidratos de carbono (g)", ""),
            "proteinas_g": data.get("proteínas (g)", ""),
            "grasas_totales_g": data.get("lípidos totales (g)", ""),
            "fuente": "Argenfood - Universidad Nacional de Luján"
        })
    except:
        continue

    time.sleep(0.3)

df = pd.DataFrame(rows)
df.to_csv("data/argenfood_base.csv", index=False)

print("✅ Scraping Argenfood completo")
print(df.head())
