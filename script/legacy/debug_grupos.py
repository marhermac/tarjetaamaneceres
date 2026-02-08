import pandas as pd

df = pd.read_csv("data/argenfood_clasificado.csv")
print("Grupos en alimentos:")
print(sorted(df["grupo"].unique()))

print("\nGrupos en porciones:")
p = pd.read_csv("data/porciones_estandar.csv")
print(sorted(p["grupo"].unique()))
