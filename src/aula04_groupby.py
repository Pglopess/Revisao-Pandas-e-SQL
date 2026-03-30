import pandas as pd

df = pd.read_csv("data/vendas.csv")
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

print (df.groupby("vendedor")["quantidade"].sum())
print ("----")
print (df.groupby("categoria")["preco_unitario"].mean())
print ("----")
print (df.groupby("produto").count())
print ("----")
print (df.groupby("produto")["data"].count())
print ("----")
print (df.groupby("vendedor")["faturamento"].sum())