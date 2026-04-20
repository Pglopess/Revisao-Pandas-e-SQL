# Revisão Pandas e SQL com Python

Este repositório contém exercícios práticos desenvolvidos para estudo de manipulação de dados em Python, com foco nas bibliotecas Pandas e SQLite.

## Tecnologias utilizadas

- Python 3.9+
- Pandas
- SQLite (sqlite3)

## Tópicos cobertos

**Pandas:** DataFrames, leitura de CSV, seleção com loc/iloc, filtragem, groupby, limpeza de dados, merge e exportação de resultados.

**SQL:** SELECT, WHERE, ORDER BY, GROUP BY, HAVING, INNER JOIN, LEFT JOIN, integração com sqlite3.

## Como rodar

1. Clone o repositório
2. Crie e ative o ambiente virtual:
```bash
   py -m venv .venv
   .venv\Scripts\activate
```
3. Instale as dependências:
```bash
   pip install -r requirements.txt
```
4. Execute qualquer script da pasta `src/`:
```bash
   py src/aula01_dataframe.py
```

## Estrutura do projeto
```
├── src/        # scripts Python organizados por aula
├── data/       # arquivos de dados (não versionados)
├── outputs/    # resultados gerados pelos scripts
└── requirements.txt
```

## Observações

Os arquivos foram desenvolvidos com foco educacional e seguem uma sequência progressiva de complexidade. Este repositório faz parte de um plano de estudos estruturado para a área de dados e backend Python.
