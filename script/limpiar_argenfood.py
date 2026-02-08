import pandas as pd
import numpy as np

# --- Config ---
INPUT = "data/argenfood_base.csv"
OUTPUT = "data/argenfood_limpio.csv"

# --- Cargar ---
df = pd.read_csv(INPUT)

# --- Función limpieza ---
def limpiar_numero(x):
    if pd.isna(x):
        return np.nan
    if isinstance(x, str):
        x = x.strip().lower()
        if x in ["nd", "traza", "tr", "-"]:
            return np.nan
        x = x.replace(",", ".")
        try:
            return float(x)
        except:
            return np.nan
    return x

# --- Columnas numéricas (ajustá según tu CSV) ---
columnas_numericas = [
    "energia_kcal",
    "hidratos_carbono_g",
    "azucares_g",
    "proteinas_g",
    "grasas_totales_g",
    "grasas_saturadas_g",
    "sodio_mg"
]

for col in columnas_numericas:
    if col in df.columns:
        df[col] = df[col].apply(limpiar_numero)

# --- Guardar ---
df.to_csv(OUTPUT, index=False)

print("✔ CSV limpio generado:", OUTPUT)
