import pandas as pd

df = pd.read_csv("data/vendas.csv")
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

df.groupby("vendedor")["faturamento"].sum().reset_index().to_csv("outputs/faturamento_por_vendedor.csv", index=False)
df.groupby("vendedor")["faturamento"].sum().reset_index().to_json("outputs/faturamento_por_vendedor.json", orient="records")
