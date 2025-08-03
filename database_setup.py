import sqlite3

with sqlite3.connect('controlezero.db') as banco_de_dados:
    cursor = banco_de_dados.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS transacoes (id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "descricao TEXT NOT NULL," \
    "valor REAL NOT NULL," \
    "categoria TEXT NOT NULL)"
    )

"""cursor.execute(
            "INSERT INTO transacoes (descricao, valor, categoria) VALUES (?, ?, ?)",
            ("Pratos", 60, "Utensílios de cozinha")
        )"""
