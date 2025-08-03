"""
    -- ControleZero V1 ---
"""
# Importando as funções e bibliotecas
from core.transacoes import *
from core.utils import *

#Iniciei a lista com 3 itens de exemplo para teste
lista_de_transacoes = [{
        "descricao" : "carvão",
        "valor" : 45,
        "categoria" : "churrasco"
    }, {
        "descricao" : "Aluguel",
        "valor" : 750,
        "categoria" : "Moradia"
    }, {
        "descricao" : "Halls",
        "valor" : 1.50,
        "categoria" : "Doces"
    }]

# Função principal do sistema
def main():
    # Inicia o loop para manter o sistema rodando
    while True:
        # Limpa a tela para melhor interface
        limpar_tela()
        # Chama a função titulo para personalizar interface
        titulo("ControleZero")
        # Lista com as opções do menu
        opcoes = ["Adicionar Nova Transação (Receita/Despesa)", "Listar Todas as Transações", "Ver Saldo Total","Sair"]
        # Lista as opções atravez da função
        listar_menu(opcoes)
        # Valida a escolha do usuario atravez da função
        opcao_escolhida_menu = escolher_opcao()
        # Controle do sistema atravez da match-case
        match opcao_escolhida_menu:
            # Opção 1= Adicionar nova transação
            case 1:
                # Inicia o loop 
                while True:
                        # Limpa a  tela para melhor interface
                        limpar_tela()
                        # Chama a função titulo para personalizar interface
                        titulo("Nova Transação")
                        # Solicita a descrição com verificação de input vazio e armazenando como lower
                        descricao = obter_input_vazio("Descrição: ").lower()
                        # Solicita o valor com verificação de input numerico 
                        valor = obter_input_float("Valor: ")
                        # Solicita a categoria com verificação de input vazio e armazenando como lower
                        categoria = obter_input_vazio("Categoria: ").lower()
                        # Chama a função para adicionar os 3 itens a lista principal
                        lista_de_transacoes.append(adicionar_transacao(descricao, valor, categoria))
                        # Imprime uma confirmação do item adicionado com formatação do valor
                        print(f"\n{descricao.capitalize()} - R${valor:.2f} - {categoria.capitalize()} | ✅")
                        # Chama a função de pausa para melhor funcionamento na interface
                        pausa_segundos(2)
                        # interrompe o loop e retorna ao menu principal
                        break
            # Opção 2 = Listar todas as ransações
            case 2:
                # Limpa a tela para melhor interface
                limpar_tela()
                # Chama a função titulo para personalizar interface
                titulo("Listar Transações")
                # Verifica se a lista principal está vazia
                if not lista_de_transacoes:
                    # Imprime uma mensagem de alerta
                    print("\nNenhum registro encotrado!")
                    # Pausa para melhor interface
                    pausa_segundos(2)
                    #Limpa a tela antes de retornar ao menu principal
                    limpar_tela()
                # Caso tenha algo na lista
                else:
                    # Loop for para passar por cada registro da lista enumerando e iniciando em 1
                    for e, itens in enumerate(lista_de_transacoes, start=1):
                        # Imprime o item de forma organizada e formatada [(Enumeração). Categoria: Descrição - Valor]
                        print(f"{e}. {itens["categoria"].capitalize()}: {itens["descricao"].capitalize()} - R${itens["valor"]:.2f}")
                    # Input para continuar o loop
                    continuar = str(input("\nAperte Enter para continuar..."))
                    # Pausa para melhor interface
                    pausa_segundos(1)
                    # Limpa a tela antes de retornar ao menu principal
                    limpar_tela()
            # Opção 3 = Calcular valor
            case 3:
                # Limpa a tela para melhor interface
                limpar_tela()
                # Chama a função titulo para personalizar interface
                titulo("Saldo Total")
                # Inicia a variavel zerada
                saldo_total = 0.0
                # Loop for para cada registro da lista principal
                for transacoes in lista_de_transacoes:
                    # Adiciona o valor da transacao ao saldo total
                    saldo_total += transacoes["valor"]
                # Imprime o saldo total formatado
                print(f"Saldo total: R${saldo_total:.2f}")
                # Input para continuar o loop
                continuar = str(input("\nAperte Enter para continuar..."))
                # Pausa para melhor interface
                pausa_segundos(1)
                # Limpa a tela antes de retornar ao menu principal
                limpar_tela()
            # Opção 4 = Finalizar programa
            case 4:
                # Limpa a tela para melhor interface
                limpar_tela()
                # Imprime uma mensagem para melhor interface
                print("Finalizando programa...")
                # Pausa para melhor interface
                pausa_segundos(1)
                # Limpa a tela antes de finalizar
                limpar_tela()
                # Interrompendo o loop principal do sistema
                break
            # Qualquer valor fora das opções anteriores
            case _:
                # Mensagem de erro
                print("Escolha inválida, selecione uma entre as opções!")
                # Pausa antes de retornar ao menu
                pausa_segundos(2)


# Condicional para verificarse script atual está sendo execurado diretamente
if __name__ == "__main__":
    main()