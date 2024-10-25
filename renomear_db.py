import pandas as pd
import sqlite3
from datetime import datetime

# Conectar ao banco de dados de origem e ler a tabela
con_origem = sqlite3.connect('banco.db')
df = pd.read_sql_query("SELECT * FROM clientes_fisicos", con_origem)

# Renomear as colunas
df = df.rename(columns={
    "ID": "id",
    "Nome": "nome",
    "Telefone": "celular",
    "Email": "email",
    "Endereço": "endereco"
})

# Adicionar coluna 'data_insercao' com a data atual
df['data_insercao'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Conectar ao banco de dados de destino
con_destino = sqlite3.connect('banco_destino.db')

# Criar a tabela `clientes_fisicos` manualmente com `id` autoincrementado
with con_destino:
    con_destino.execute('''
    CREATE TABLE IF NOT EXISTS clientes_fisicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        celular TEXT,
        email TEXT,
        endereco TEXT,
        data_insercao TEXT
    )
    ''')

# Inserir dados no banco, excluindo a coluna `id` para que seja gerada automaticamente
df = df.drop(columns=['id'])  # Remove a coluna `id` do DataFrame
df.to_sql('clientes_fisicos', con_destino, if_exists='append', index=False)

# Fechar conexões
con_origem.close()
con_destino.close()

print("Dados transferidos com IDs únicos gerados automaticamente!")
