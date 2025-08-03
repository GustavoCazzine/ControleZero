import sqlite3

banco_de_dados = sqlite3.connect("controlezero.db")
cursor = banco_de_dados.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS transacoes (id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "descricao TEXT NOT NULL," \
    "valor REAL NOT NULL," \
    "categoria TEXT NOT NULL)"
    )

banco_de_dados.commit()