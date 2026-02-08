import pandas as pd
import numpy as np

# 1. CARGA DE DATOS
# Cargamos el archivo sucio que acabamos de generar
df = pd.read_csv('dirty_data_challenge.csv')

print("--- Resumen Inicial de Datos Sucios ---")
print(df.info())
print("\nPrimeras 5 filas:")
print(df.head())

# ==========================================
# 2. LIMPIEZA DE COLUMNA 'COUNTRY'
# Normalizamos nombres de países usando un mapeo lógico
# ==========================================
mapeo_paises = {
    'argentina': 'Argentina', 'arg': 'Argentina', 'arg.': 'Argentina', 'arg': 'Argentina',
    'ee.uu': 'USA', 'usa': 'USA', 'united states': 'USA', 'u.s.': 'USA', 'u.s.a': 'USA'
}

# Pasamos a minúsculas, quitamos espacios y aplicamos el diccionario
df['Country'] = df['Country'].str.lower().str.strip().map(mapeo_paises).fillna('Sin Definir')

# ==========================================
# 3. LIMPIEZA DE PRECIOS (De texto a número real)
# El mayor dolor de cabeza en inventarios: símbolos y puntos/comas
# ==========================================
def limpiar_precio(precio):
    if pd.isna(precio): return 0.0
    # Quitamos el signo $, espacios, y corregimos separadores
    p = str(precio).replace('$', '').replace(' ', '')
    # Si viene con formato 1.200,50 -> lo pasamos a 1200.50
    p = p.replace('.', '').replace(',', '.')
    return float(p)

df['Price'] = df['Price'].apply(limpiar_precio)

def corregir_fechas(fecha):
    if pd.isna(fecha): return pd.NaT
    # Intentamos los formatos más comunes en este dataset
    for fmt in ('%Y-%m-%d', '%d/%m/%y', '%Y.%m.%d', '%m-%d-%Y', '%B %dst %Y'):
        try:
            return pd.to_datetime(fecha, format=fmt)
        except:
            continue
    # Si nada funciona, dejamos que pandas lo intente solo
    return pd.to_datetime(fecha, errors='coerce')

df['Date'] = df['Date'].apply(corregir_fechas)

df = df.drop_duplicates()






print("\n--- Precios después de la limpieza (Primeras 5) ---")
print(df['Price'].head())

# ==========================================
# 4. NORMALIZACIÓN DE FECHAS
# El desafío: formatos mezclados (2023.05.01, May 1st, 01/05/23)
# ==========================================
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# ==========================================
# 5. LIMPIEZA DE IDs Y CATEGORÍAS
# Quitamos espacios invisibles y unificamos mayúsculas
# ==========================================
df['ID_Producto'] = df['ID_Producto'].str.strip().str.upper()
df['Category'] = df['Category'].str.strip().str.capitalize().fillna('Sin Categoría')

# ==========================================
# 6. DEDUPLICACIÓN
# Una vez limpios los IDs, podemos ver los duplicados reales
# ==========================================
filas_antes = len(df)
df = df.drop_duplicates()
filas_despues = len(df)

# ==========================================
# 7. EXPORTACIÓN FINAL
# Guardamos el archivo limpio para el portfolio
# ==========================================
df.to_csv('clean_data_final.csv', index=False)

print("\n--- Auditoría Final ---")
print(f"Filas originales: {filas_antes}")
print(f"Filas tras eliminar duplicados: {filas_despues}")
print(f"Datos nulos restantes en Fecha: {df['Date'].isna().sum()}")
print("\nPrimeras 5 filas del archivo LIMPIO:")
print(df.head())
print("\n¡Archivo 'clean_data_final.csv' generado con éxito!")
