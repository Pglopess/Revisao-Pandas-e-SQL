import pandas as pd

df = pd.read_csv("data/vendas.csv")

print (df["produto"])
print ("----")
print (df[["vendedor", "quantidade"]])
print ("----")
print (df[df["vendedor"] == "Ana"])
print ("----")
print (df.iloc[0:3])
print ("----")
print (df.loc[:, ["produto", "preco_unitario"]])
print ("----")
print (df.loc[5])