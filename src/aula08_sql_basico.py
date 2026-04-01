import sqlite3

conn = sqlite3.connect('data/vendas.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS produtos")
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
     id INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL
)''')

cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES ('Notebook', 'Eletrônicos', 2500.00)")
cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES ('Smartphone', 'Eletrônicos', 1500.00)")
cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES ('Cadeira', 'Móveis', 300.00)")
cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES ('Mesa', 'Móveis', 500.00)")
cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())
conn.commit()