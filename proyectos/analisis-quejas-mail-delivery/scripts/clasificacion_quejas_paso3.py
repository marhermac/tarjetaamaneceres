import pandas as pd

# ----------------------------
# 1. Carga de dataset limpio
# ----------------------------
input_path = "data/processed/mails_limpios_paso2.csv"
df = pd.read_csv(input_path)

print("Registros analizados:", len(df))

# ----------------------------
# 2. Función de clasificación
# ----------------------------
def clasificar_queja(asunto):
    asunto = asunto.lower()

    if any(palabra in asunto for palabra in ["tarde", "demora", "retraso", "no llego"]):
        return "Retraso en la entrega"

    if any(palabra in asunto for palabra in ["incompleto", "faltante", "falta producto"]):
        return "Pedido incompleto"

    if any(palabra in asunto for palabra in ["roto", "mal estado", "derramado", "vencido"]):
        return "Producto en mal estado"

    if any(palabra in asunto for palabra in ["repartidor", "cadete", "moto", "trato"]):
        return "Problemas con el repartidor"

    if any(palabra in asunto for palabra in ["cobro", "factura", "precio", "me cobraron"]):
        return "Cobro o facturación"

    return "Otros"

# ----------------------------
# 3. Aplicación de clasificación
# ----------------------------
df['tipo_queja'] = df['asunto_limpio'].apply(clasificar_queja)

# ----------------------------
# 4. Análisis de popularidad
# ----------------------------
# Total por tipo de queja
ranking_quejas = (
    df.groupby('tipo_queja')
      .size()
      .reset_index(name='cantidad')
      .sort_values(by='cantidad', ascending=False)
)

# Popularidad por fecha
quejas_por_fecha = (
    df.groupby(['fecha', 'tipo_queja'])
      .size()
      .reset_index(name='cantidad')
)

# Popularidad por zona
quejas_por_zona = (
    df.groupby(['zona', 'tipo_queja'])
      .size()
      .reset_index(name='cantidad')
)

# ----------------------------
# 5. Exportación de resultados
# ----------------------------
ranking_quejas.to_csv("data/analysis/ranking_quejas.csv", index=False)
quejas_por_fecha.to_csv("data/analysis/quejas_por_fecha.csv", index=False)
quejas_por_zona.to_csv("data/analysis/quejas_por_zona.csv", index=False)

print("\nTop quejas:")
print(ranking_quejas.head())

print("\nArchivos generados en /analysis:")
print("- ranking_quejas.csv")
print("- quejas_por_fecha.csv")
print("- quejas_por_zona.csv")
