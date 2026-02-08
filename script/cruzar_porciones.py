import pandas as pd

# --- Archivos ---
ALIMENTOS = "data/argenfood_clasificado.csv"
PORCIONES = "data/porciones_estandar.csv"
OUTPUT = "data/argenfood_porciones.csv"

# --- Cargar ---
df = pd.read_csv(ALIMENTOS)
porciones = pd.read_csv(PORCIONES)

# --- Merge por grupo ---
df = df.merge(porciones, on="grupo", how="left")

# --- Fallback seguro ---
df["porcion_g"] = df["porcion_g"].fillna(50)

# --- Calcular carbohidratos por porción ---
df["carbohidratos_por_porcion"] = (
    df["carbohidratos_g"] * df["porcion_g"] / 100
)

# --- Guardar ---
df.to_csv(OUTPUT, index=False)

print("✅ Porciones aplicadas")
print(df[["grupo", "porcion_g"]].drop_duplicates().head())
