import os
from time import sleep

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pausa_segundos(segundos):
    sleep(segundos)

def titulo(msg):
    print(f" --- {msg} ---\n")

def obter_input_vazio(prompt):
    while True:
        resposta_usuario = input(prompt).strip()
        if resposta_usuario:
            return resposta_usuario
        print("\nErro: Campo não pode ser vazio")
        pausa_segundos(2)

def obter_input_float(prompt):
    while True:
        resposta_usuario = input(prompt)
        try:
            return float(resposta_usuario)
        except ValueError:
            print("\nErro: Valor digitado não é númerico")
            pausa_segundos(2)
        except Exception as i:
            print("\nOcorreu um erro:", i)
            pausa_segundos(2)

def listar_menu(opcoes):
    for e, opcao in enumerate(opcoes, start=1):
        print(f"{e}. {opcao}")

def escolher_opcao():
    while True:
        try:
            escolha_usuario = int(input("\nEscolha uma opção: "))
            return escolha_usuario
        except ValueError:
            print("\nErro: Valor digitado não é númerico")
            pausa_segundos(2)
        except Exception as i:
            print("\nOcorreu um erro:", i)
            pausa_segundos(2)