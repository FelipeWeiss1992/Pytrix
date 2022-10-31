import os

def salvar_itens(bomboniere):
    with open("registro_cliente.txt", "a") as arquivo:
        arquivo.write(f"{bomboniere}\n")


def salvar_pagamento(forma_pagamento):
    with open("registro_cliente.txt", "a") as arquivo:
        arquivo.write(f"{forma_pagamento}\n")


def ticket():
    # Limpa a tela
    os.system("cls")
    # Abre o arquivo
    with open("registro_cliente.txt", "r") as arquivo:
        # Percorre as linhas do arquivo
        for linha in arquivo:
            # Transforma cada linha em um Dicionário
            dicio = eval(linha)
            # Percorre o Dicionário
            for chave, valor in dicio.items():
                # Verifica se é a primeira chave de cada Dicionário
                if chave == "Pipoca":
                    # Imprimi a Label Bomboniere
                    print("\n- Bomboniere\n")
                # Verifica se é a primeira chave de cada Dicionário
                if chave == "Pagamento":
                    # Imprimi a Lacel Forma de pagamento
                    print("\n- Forma de pagamento\n")
                # Imprime as Chaves e Valores do Dicionário
                print(f"   * {chave} ----- {valor}")

        # Imprime a saudação final
        print("\n", "-" * 5, "Volte Sempre", "-" * 5)