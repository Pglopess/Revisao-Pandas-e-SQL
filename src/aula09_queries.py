import sqlite3
import pandas as pd

conn = sqlite3.connect("data/vendas.db")
cursor = conn.cursor()

# Recria a tabela com mais dados
cursor.execute("DROP TABLE IF EXISTS vendas")
cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY,
    vendedor TEXT,
    produto TEXT,
    categoria TEXT,
    quantidade INTEGER,
    preco_unitario REAL,
    data TEXT
)''')

vendas = [
    ("Ana", "Notebook", "Eletrônicos", 2, 3500.00, "2024-01-03"),
    ("Bruno", "Mouse", "Periféricos", 5, 89.90, "2024-01-05"),
    ("Ana", "Teclado", "Periféricos", 3, 199.90, "2024-01-05"),
    ("Carlos", "Monitor", "Eletrônicos", 1, 1200.00, "2024-01-08"),
    ("Bruno", "Notebook", "Eletrônicos", 1, 3500.00, "2024-01-10"),
    ("Carlos", "Mouse", "Periféricos", 8, 89.90, "2024-01-12"),
    ("Bruno", "Teclado", "Periféricos", 2, 199.90, "2024-01-15"),
    ("Ana", "Monitor", "Eletrônicos", 2, 1200.00, "2024-01-18"),
    ("Carlos", "Notebook", "Eletrônicos", 3, 3500.00, "2024-01-20"),
    ("Ana", "Mouse", "Periféricos", 4, 89.90, "2024-01-22"),
]

cursor.executemany("INSERT INTO vendas (vendedor, produto, categoria, quantidade, preco_unitario, data) VALUES (?, ?, ?, ?, ?, ?)", vendas)
conn.commit()

df = pd.read_sql("SELECT * FROM vendas WHERE categoria = 'Eletrônicos'", conn)
print(df)
print("----")

df = pd.read_sql("SELECT vendedor, produto, quantidade FROM vendas ORDER BY quantidade DESC", conn)
print(df)
print("----")

df = pd.read_sql("SELECT vendedor, SUM(quantidade * preco_unitario) AS total_vendas FROM vendas GROUP BY vendedor", conn)
print(df)
print("----")

df = pd.read_sql("SELECT vendedor FROM vendas GROUP BY vendedor HAVING SUM(quantidade) > 10", conn)
print(df)
print("----")

df = pd.read_sql("SELECT categoria, SUM(quantidade * preco_unitario) AS faturamento_total FROM vendas GROUP BY categoria", conn)
print(df)
print("----")