import pandas as pd

df = pd.read_csv("data/vendas_sujas.csv")
df = df.drop_duplicates()
df = df.fillna({"vendedor": "Desconhecido"})
df = df.fillna({"quantidade": 0})
df = df.dropna()  # remove o que sobrou de nulo

print(df)
print("----")
print(df.isnull().sum())
print ("----")
print(df.duplicated().sum())
print ("----")
print(df.dtypes)