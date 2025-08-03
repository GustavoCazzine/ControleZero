import sqlite3

banco_de_dados = sqlite3.connect("controlezero.db")
cursor = banco_de_dados.cursor()

def adicionar_transacao(descricao, valor, categoria):
    try:
        cursor.execute(
            "INSERT INTO transacoes (descricao, valor, categoria) VALUES (?, ?, ?)",
            (descricao, valor, categoria)
        )
        return True
    except:
        return False

def listar_todas_transacoes():
    cursor.execute("SELECT * FROM transacoes")
    linhas = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    # Lista inicial de transações
    lista_de_transacoes = []    
    for linha in linhas:
        dicionario = dict(zip(colunas, linha))
        lista_de_transacoes.append(dicionario)

    return lista_de_transacoes

def calcular_saldo_total():
    lista_de_transacoes = listar_todas_transacoes()
    saldo_total = sum(transacao["valor"] for transacao in lista_de_transacoes)
    return saldo_total
        
