# Importando funções e bibliotecas
import os
from time import sleep

# Função para limpar a tela
def limpar_tela():
    if os.name == 'nt': # Para Windows
        os.system('cls')
    else: # Para Linux/macOS
        os.system('clear')

# Função para uma pausa no terminal, que recebe parametros de segundos de pausa
def pausa_segundos(segundos):
    sleep(segundos)

# Função para titulo padronizado, recebe parametros do titulo a ser exibido
def titulo(msg):
    print(f" --- {msg} ---\n")

# Função para detectar input vazio, que recebe parametros da pergunta solicitada
def obter_input_vazio(prompt):
    # Loop para manter o input enquanto não estiver correto
    while True:
        try:
            # armazena a resposta do input 
            resposta_usuario = input(prompt).strip()
            #Remove espaços no inicio/fim e verifica se campo está vazio
            if not resposta_usuario.strip():
                raise ValueError("Campo não pode ser vazio")
                pausa_segundos(2)
                limpar_tela()
            # Retorna a resposta caso preenchida
            else:
                return resposta_usuario
            # Erros e exceções
        except ValueError as e:
            print("\nErro:", e)
            pausa_segundos(2)
            print()
        except Exception as e:
            print("\nOcorreu um erro:", e)
            pausa_segundos(2)
            print()

# Função para detectar se input é númerico, que recebe parametros da pergunta solicitada
def obter_input_float(prompt):
    # Loop para manter o input enquanto não estiver correto
    while True:
        # Armazena a resposta do input
        resposta_usuario = input(prompt)
        # Tenta converter resposta para float
        try:
            # Retorna a resposta caso seja numerico
            return float(resposta_usuario)
        # Erros e exceções
        except ValueError:
            print("\nErro: Valor digitado não é númerico")
            pausa_segundos(2)
        except Exception as i:
            print("\nOcorreu um erro:", i)
            pausa_segundos(2)

# Função para listas as opçoes do menu, que recebe parametros de uma lista com todas as opçoes
def listar_menu(opcoes):
    # Loop for para exibir todas as opçoes da lista
    for e, opcao in enumerate(opcoes, start=1):
        print(f"{e}. {opcao}")

# Função para validar a opção escolhida do usuario
def escolher_opcao():
    # Loop para manter o usuario enquanto resposta não for correta
    while True:
        try:
            # armazena a resposta do input
            escolha_usuario = int(input("\nEscolha uma opção: "))
            # Retorna a resposta
            return escolha_usuario
        # Erros e exceções
        except ValueError:
            print("\nErro: Valor digitado não é númerico")
            pausa_segundos(2)
        except Exception as i:
            print("\nOcorreu um erro:", i)
            pausa_segundos(2)