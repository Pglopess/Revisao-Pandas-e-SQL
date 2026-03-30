import pandas as pd

vendedores = pd.DataFrame({
    "vendedor_id": [1, 2, 3, 4],
    "nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "regiao": ["Sul", "Norte", "Sul", "Leste"]
})

vendas = pd.DataFrame({
    "venda_id": [101, 102, 103, 104, 105],
    "vendedor_id": [1, 2, 1, 3, 1],
    "valor": [3500, 89, 1200, 199, 3500]
})

print(pd.merge(vendedores, vendas, on="vendedor_id", how="inner"))  
print("----")
print(pd.merge(vendedores, vendas, on="vendedor_id", how="left"))
