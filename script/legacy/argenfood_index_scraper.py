import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.argenfood.unlu.edu.ar/Tablas/Codigo/Ranking/"

r = requests.get(URL, timeout=15)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

rows = []

for a in soup.select("a"):
    href = a.get("href", "")
    texto = a.get_text(strip=True)

    if "/Tablas/Tabla/" in href and texto:
        rows.append({
            "alimento": texto,
            "url": "https://www.argenfood.unlu.edu.ar" + href
        })

df = pd.DataFrame(rows).drop_duplicates()

df.to_csv("data/argenfood_index.csv", index=False)

print("✅ Índice generado")
print(df.head())
print("Total alimentos:", len(df))
