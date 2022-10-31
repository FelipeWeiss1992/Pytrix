import os

def limpaarquivo():
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "w") as arquivo:
        # Salva o Dicionário do arquivo
        arquivo.write("")

# Função para registrar a escolha da bomboniere
def salvar_itens(bomboniere):
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "a") as arquivo:
        # Salva o Dicionário do arquivo
        arquivo.write(f"{bomboniere}\n")


# Função para registrar a forma de pagamento
def salvar_pagamento(forma_pagamento):
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "a") as arquivo:
        # Salva o Dicionário do arquivo
        arquivo.write(f"{forma_pagamento}\n")


# Função para impressão do ticket do cliente 
def ticket():
    # Limpa a tela
    os.system("cls")
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "r") as arquivo:
        # Percorre as linhas do arquivo
        for linha in arquivo:
            # Transforma cada linha em um Dicionário
            dicio = eval(linha)
            # Percorre o Dicionário
            for chave, valor in dicio.items():
                if chave == "nome":
                    print("\n- Cliente Premium\n")

                if chave == "filme":
                    print("\n- Seu Filme\n")
                
                if chave == "Poltrona":
                    print("\n- Sua Poltrona\n")

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