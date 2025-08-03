from core.transacoes import adicionar_transacao
from core.utils import limpar_tela, titulo, listar_menu, escolher_opcao, obter_input_vazio, obter_input_float, pausa_segundos

# Lista inicial de transações para teste
lista_de_transacoes = [
    {"descricao": "carvão", "valor": 45, "categoria": "churrasco"},
    {"descricao": "Aluguel", "valor": 750, "categoria": "Moradia"},
    {"descricao": "Halls", "valor": 1.50, "categoria": "Doces"}
]

def main():
    while True:
        limpar_tela()
        titulo("ControleZero")
        opcoes = [
            "Adicionar Nova Transação (Receita/Despesa)",
            "Listar Todas as Transações",
            "Ver Saldo Total",
            "Sair"
        ]
        listar_menu(opcoes)
        opcao_escolhida_menu = escolher_opcao()
        match opcao_escolhida_menu:
            case 1:
                limpar_tela()
                titulo("Nova Transação")
                descricao = obter_input_vazio("Descrição: ").lower()
                valor = obter_input_float("Valor: ")
                categoria = obter_input_vazio("Categoria: ").lower()
                lista_de_transacoes.append(adicionar_transacao(descricao, valor, categoria))
                print(f"\n{descricao.capitalize()} - R${valor:.2f} - {categoria.capitalize()} | ✅")
                pausa_segundos(2)
            case 2:
                limpar_tela()
                titulo("Listar Transações")
                if not lista_de_transacoes:
                    print("\nNenhum registro encotrado!")
                    pausa_segundos(2)
                    limpar_tela()
                else:
                    for e, itens in enumerate(lista_de_transacoes, start=1):
                        print(f"{e}. {itens['categoria'].capitalize()}: {itens['descricao'].capitalize()} - R${itens['valor']:.2f}")
                    input("\nAperte Enter para continuar...")
                    pausa_segundos(1)
                    limpar_tela()
            case 3:
                limpar_tela()
                titulo("Saldo Total")
                saldo_total = sum(transacao["valor"] for transacao in lista_de_transacoes)
                print(f"Saldo total: R${saldo_total:.2f}")
                input("\nAperte Enter para continuar...")
                pausa_segundos(1)
                limpar_tela()
            case 4:
                limpar_tela()
                print("Finalizando programa...")
                pausa_segundos(1)
                limpar_tela()
                break
            case _:
                print("Escolha inválida, selecione uma entre as opções!")
                pausa_segundos(2)

if __name__ == "__main__":
    main()