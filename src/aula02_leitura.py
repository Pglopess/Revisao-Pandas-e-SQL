import pandas as pd

df = pd.read_csv("data/vendas.csv")

print (df)
print ("----")
print(type(df))
print ("----")
print(df.shape)
print ("----")
print (df.dtypes)
