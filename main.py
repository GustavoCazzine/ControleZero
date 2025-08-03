"""
    -- ControleZero V1 ---
"""

from core.transacoes import *
import os
from time import sleep

def limpar_tela():
    if os.name == 'nt': # Para Windows
        os.system('cls')
    else: # Para Linux/macOS
        os.system('clear')

def pausa_segundos(segundos):
    sleep(segundos)

def titulo(msg):
    print(f" --- {msg} ---\n")

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

def main():
    while True:
        limpar_tela()

        titulo("ControleZero")

        print("1. Adicionar Transação (Receita/Despesa)\n2. Listar Todas as Transações\n3. Ver Saldo Total\n4. Sair")

        try:

            opcao_escolhida_menu = int(input("Escolha uma opção: "))

            match opcao_escolhida_menu:
                case 1:
                    transacao_concluida = False
                    while True:
                        if not transacao_concluida:
                            limpar_tela()
                            titulo("Nova Transação")


                            try:
                                descricao = str(input("Descrição: ")).lower()

                                if not descricao.strip():
                                    raise ValueError("\nCampo não pode ser vazio")
                                    pausa_segundos(2)
                                else:
                                    while True:
                                        if not transacao_concluida:
                                            try:
                                                valor = float(input("Valor: "))

                                                while True:
                                                    if not transacao_concluida:
                                                        try:
                                                            categoria = str(input("Categoria: ")).lower()

                                                            if not categoria.strip():
                                                                raise ValueError("\nCampo não pode ser vazio")
                                                                pausa_segundos(2)
                                                            else:
                                                                
                                                                try:
                                                                    lista_de_transacoes.append(adicionar_transacao(descricao, valor, categoria))
                                                                    print(f"\n{descricao.capitalize()} - R${valor:.2f} - {categoria.capitalize()} | ✅")
                                                                    transacao_concluida = True
                                                                    pausa_segundos(2)

                                                                except:
                                                                    print("\nErro inesperado ao adicionar transação! Tente novamente.")
                                                        except ValueError as c:
                                                            print("\nErro:", c)
                                                            pausa_segundos(2)
                                                        except Exception as c:
                                                            print("\nOcorreu um erro:", c)
                                                            pausa_segundos(2)
                                                    else:
                                                        break

                                            except ValueError:
                                                print("\nErro: Valor digitado não é númerico")
                                                pausa_segundos(2)
                                            except Exception as i:
                                                print("\nOcorreu um erro:", i)
                                                pausa_segundos(2)
                                        else:
                                            break

                            except ValueError as e:
                                print("\nErro:", e)
                                pausa_segundos(2)
                            except Exception as e:
                                print("\nOcorreu um erro:", e)
                                pausa_segundos(2)
                        else:
                            break
                case 2:
                    limpar_tela()
                    titulo("Listar Transações")

                    if not lista_de_transacoes:
                        print("\nNenhum registro encotrado!")
                        pausa_segundos(2)
                        limpar_tela()
                    else:
                        for e, itens in enumerate(lista_de_transacoes, start=1):
                            print(f"{e}. {itens["categoria"].capitalize()}: {itens["descricao"].capitalize()} - R${itens["valor"]:.2f}")

                        continuar = str(input("\nAperte Enter para continuar..."))
                        pausa_segundos(1)
                        limpar_tela()

                case 3:
                    saldo_total = 0.0
                    for transacoes in lista_de_transacoes:
                        saldo_total += transacoes["valor"]

                    print(f"Saldo total: R${saldo_total:.2f}")

                    continuar = str(input("\nAperte Enter para continuar..."))
                    pausa_segundos(1)
                    limpar_tela()
                    
                case 4:
                    print("Finalizando programa...")
                    pausa_segundos(1)
                    limpar_tela()
                    break

                case _:
                    print("Escolha inválida, selecione uma entre as opções!")
                    pausa_segundos(2)

        except ValueError:
            print("Escolha uma opção válida! Tente novamente.")
            pausa_segundos(2)



if __name__ == "__main__":
    main()