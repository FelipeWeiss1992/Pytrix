
def salvar_itens(bomboniere):
    with open("registro_cliente.txt", "a") as arquivo:
        arquivo.write(f"{bomboniere}\n")

    print(bomboniere)


def salvar_pagamento(forma_pagamento):
    with open("registro_cliente.txt", "a") as arquivo:
        arquivo.write(f"{forma_pagamento}\n")


def ticket():
    with open("registro_cliente.txt", "r") as arquivo:
        # Percorre as linhas do arquivo
        for linha in arquivo:
            # Transforma cada linha em uma Lista
            lista = eval(linha)
            print(lista)
            # Percorre a lista



"""
# Definição da Função recebendo kwargs
def funcao(**kwargs):
    # Percorrendo argumento nomeados
    for chave in kwargs:
        print(f"Acessando Chave '{chave}', valor = {kwargs.get(chave)}")

regulagem = {'max': 10, 'meio': 5, 'min': 0}

funcao(**regulagem)
"""