from poplib import CR
import sqlite3
def criar_tabela(data, categoria, valor, descricao, forma_de_pagamento):
        # Conectar ao banco de dados (cria o arquivo se não existir)
    conexao = sqlite3.connect('gastos.db')
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()
    # Criar a tabela de gastos (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            categoria TEXT,
            valor REAL,
            descricao TEXT,
            forma_de_pagamento TEXT
        )
    ''')
    # Fechar a conexão
    conexao.commit()
    conexao.close()