import pandas as pd

df = pd.read_csv("data/vendas.csv")

print (df["produto"])
print ("----")
print (df[["vendedor", "quantidade"]])
print ("----")
print (df[df["vendedor"] == "Ana"])