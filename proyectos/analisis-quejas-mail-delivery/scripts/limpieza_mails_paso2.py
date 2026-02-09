import pandas as pd
import re

# ----------------------------
# 1. Carga de datos
# ----------------------------
input_path = "data/raw/mails_quejas_raw.csv"
df = pd.read_csv(input_path)

print("Registros originales:", len(df))

# ----------------------------
# 2. Normalización de fechas
# ----------------------------
df['fecha'] = pd.to_datetime(
    df['fecha_raw'],
    errors='coerce',
    dayfirst=True
)


# Nos quedamos solo con la fecha (sin hora)
df['fecha'] = df['fecha'].dt.date

# ----------------------------
# 3. Limpieza del asunto
# ----------------------------
def limpiar_asunto(texto):
    if pd.isna(texto):
        return "sin asunto"

    texto = texto.lower()
    texto = re.sub(r"re:\s*", "", texto)   # elimina "re:"
    texto = re.sub(r"[^\w\s]", "", texto)  # elimina signos
    texto = texto.strip()
    return texto

df['asunto_limpio'] = df['asunto_raw'].apply(limpiar_asunto)

# ----------------------------
# 4. Selección de columnas clave
# ----------------------------
df_limpio = df[[
    'fecha',
    'asunto_limpio',
    'zona'
]]

# ----------------------------
# 5. Eliminación de filas inválidas
# ----------------------------
df_limpio = df_limpio.dropna(subset=['fecha'])

# ----------------------------
# 6. Exportación
# ----------------------------
output_path="data/processed/mails_limpios_paso2.csv"
df_limpio.to_csv(output_path, index=False, encoding="utf-8")

print("Dataset limpio generado:", output_path)
print("Registros finales:", len(df_limpio))
print("\nEjemplo:")
print(df_limpio.head())
