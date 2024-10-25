import pandas as pd
import sqlite3

# Carregar o arquivo Excel
caminho_excel = 'clientes_fisicos.xlsx'  # Substitua pelo caminho do seu arquivo Excel
df = pd.read_excel(caminho_excel)  # Coloque o nome da aba ou remova para pegar a primeira

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('banco.db')  # Substitua pelo nome do seu banco de dados

# Converter o DataFrame para uma tabela SQL
df.to_sql('clientes_fisicos', conn, if_exists='replace', index=False)  # Ajuste o nome da tabela

# Fechar a conexão com o banco de dados
conn.close()
