# Função para adicionar a descricao, valor e categoria, retornando um dicionario
def adicionar_transacao(descricao, valor, categoria):
    # Formata os parametros em um dicionario
    transacao = {
        "descricao" : descricao,
        "valor" : valor,
        "categoria" : categoria
    }
    # Retorna o dicionario
    return transacao
