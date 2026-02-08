import pandas as pd
import numpy as np
import random

# 1. Configuración de datos sucios
n_rows = 5000
paises_sucios = ['argentina', 'arg', 'Arg.', 'EE.UU', 'usa', 'united states', 'U.S.', 'u.s.a', 'ARG', 'USA']
fechas_sucias = ['2023-05-01', '01/05/23', 'May 1st 2023', '05-01-2023', '2023.05.01']

data = {
    'ID_Producto': [f" PROD_{random.randint(100, 110)} " for _ in range(n_rows)], # Espacios y pocos IDs para generar duplicados
    'Country': [random.choice(paises_sucios) for _ in range(n_rows)],
    'Price': [f"$ {random.uniform(100, 5000):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') for _ in range(n_rows)], # Formato moneda roto
    'Date': [random.choice(fechas_sucias) for _ in range(n_rows)],
    'Category': [random.choice(['Electronics', 'Home', None, '  office  ', 'ELECTRONICS']) for _ in range(n_rows)]
}

# 2. Crear DataFrame y agregar filas vacías (Nulos)
df_sucio = pd.DataFrame(data)
for col in df_sucio.columns:
    df_sucio.loc[df_sucio.sample(frac=0.1).index, col] = np.nan # 10% de nulos aleatorios

# 3. Guardar el archivo "sucio"
df_sucio.to_csv('dirty_data_challenge.csv', index=False)
print("¡Archivo 'dirty_data_challenge.csv' generado con éxito!")