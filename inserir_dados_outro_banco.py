import sqlite3

# Conectar ao banco de dados de origem (onde está a tabela clientes_fisicos)
con_origem = sqlite3.connect('banco_destino.db')
# Conectar ao banco de dados de destino (Banco.db)
con_destino = sqlite3.connect('Banco.db')

with con_origem, con_destino:
    # Apagar todos os dados existentes na tabela cadastro_cliente
    con_destino.execute("DELETE FROM cadastro_cliente")
    
    # Selecionar todos os dados da tabela clientes_fisicos
    dados = con_origem.execute("SELECT * FROM clientes_fisicos").fetchall()
    
    # Inserir os dados na tabela cadastro_cliente
    con_destino.executemany('''
        INSERT INTO cadastro_cliente (id, nome, celular, email, endereco, data_insercao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', dados)

# Fechar as conexões
con_origem.close()
con_destino.close()

print("Dados transferidos para a tabela cadastro_cliente com sucesso!")
