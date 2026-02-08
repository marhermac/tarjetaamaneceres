import pandas as pd

# =========================
# Configuración de archivos
# =========================
INPUT = "data/argenfood_limpio.csv"
OUTPUT = "data/argenfood_riga.csv"

# =========================
# Regla RIGA basada en carbohidratos (g / 100 g)
# =========================
def riga_carbohidratos(valor):
    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return "sin_dato"

    if valor <= 10:
        return "verde"
    elif valor <= 25:
        return "amarillo"
    else:
        return "rojo"

# =========================
# Estrellas y etiqueta corta
# =========================
def riga_estrella(color):
    return {
        "verde": 3,
        "amarillo": 2,
        "rojo": 1
    }.get(color, 0)

def riga_texto(color):
    return {
        "verde": "Bajo impacto glucémico",
        "amarillo": "Impacto glucémico medio",
        "rojo": "Alto impacto glucémico",
        "sin_dato": "Datos insuficientes"
    }.get(color, "Datos insuficientes")

# =========================
# Proceso
# =========================
df = pd.read_csv(INPUT)

df["carbohidratos_porcion"] = (
    df["carbohidratos_g"] * df["porcion_g"] / 100
)


# Color RIGA
df["riga_color"] = df["carbohidratos_g"].apply(riga_carbohidratos)

# Estrellas
df["riga_estrellas"] = df["riga_color"].apply(riga_estrella)

# Texto descriptivo
df["riga_descripcion"] = df["riga_color"].apply(riga_texto)

# Guardar resultado
df.to_csv(OUTPUT, index=False, encoding="utf-8")

print("✅ RIGA calculado correctamente")
print(f"📁 Archivo generado: {OUTPUT}")
print("📊 Resumen:")
print(df["riga_color"].value_counts(dropna=False))
