from core.transacoes import adicionar_transacao, listar_todas_transacoes, calcular_saldo_total
from core.utils import limpar_tela, titulo, listar_menu, escolher_opcao, obter_input_vazio, obter_input_float, pausa_segundos

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
                confirmação_db = adicionar_transacao(descricao, valor, categoria)
                if confirmação_db:
                    print(f"\n{descricao.capitalize()} - R${valor:.2f} - {categoria.capitalize()} | ✅")
                else:
                    print("Erro inesperado! Tente novamente.")
                    pausa_segundos(2)
            case 2:
                limpar_tela()
                titulo("Listar Transações")
                lista_de_transacoes = listar_todas_transacoes()
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
                saldo_total = calcular_saldo_total()
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