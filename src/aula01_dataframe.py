import pandas as pd

# Criando um DataFrame manualmente
dados = {
    "produto" : ["Notebook", "Mouse", "Teclado", "Monitor"],
    "preco" : [3500.00, 89.90, 199.90, 1200.00],
    "estoque" : [10, 45, 30, 8]
}

df = pd.DataFrame(dados)

print (df)
print ("----")
print(type(df))
print ("----")
print(df.shape)
print ("----")
print (df.dtypes)