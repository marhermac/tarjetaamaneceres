import pandas as pd

# --- Archivos ---
INPUT = "data/argenfood_base.csv"
OUTPUT = "data/argenfood_clasificado.csv"

# --- Cargar datos ---
df = pd.read_csv(INPUT)

# 🔑 Forzar texto y normalizar
df["alimento"] = df["alimento"].fillna("").astype(str)
df["alimento_norm"] = df["alimento"].str.lower()

# --- Reglas por palabras clave ---
REGLAS = {
    "verduras": ["lechuga", "tomate", "cebolla", "zanahoria", "espinaca", "acelga", "zapallo", "brocoli"],
    "frutas": ["manzana", "banana", "pera", "naranja", "mandarina", "frutilla", "durazno"],
    "legumbres": ["lenteja", "garbanzo", "poroto", "soja", "arveja"],
    "tuberculos": ["papa", "batata", "mandioca"],
    "cereales": ["arroz", "fideos", "pasta", "maiz", "avena"],
    "panificados": ["pan", "galleta", "tostada", "factura"],
    "carnes": ["carne", "pollo", "vaca", "cerdo"],
    "pescados": ["pescado", "atun", "merluza"],
    "huevos": ["huevo"],
    "lacteos": ["leche", "yogur", "yogurt"],
    "quesos": ["queso"],
    "aceites": ["aceite", "manteca", "margarina"],
    "azucares": ["azucar", "miel"],
    "dulces": ["dulce", "mermelada", "chocolate"],
    "bebidas": ["bebida", "jugo", "gaseosa"],
}

def clasificar(alimento):
    for grupo, palabras in REGLAS.items():
        if any(p in alimento for p in palabras):
            return grupo
    return "ultraprocesados"

# --- Aplicar ---
df["grupo"] = df["alimento_norm"].apply(clasificar)

# --- Limpiar ---
df.drop(columns=["alimento_norm"], inplace=True)

# --- Guardar ---
df.to_csv(OUTPUT, index=False)

print("✅ Clasificación terminada")
print(df["grupo"].value_counts())
