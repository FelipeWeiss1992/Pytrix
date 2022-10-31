# importando biblioteca
from time import sleep
# importando as funcoes
from controller import saudacao, cadastrarcliente

# definindo a função Menu
def menu():
    # chamando a funcao saudação da controller
    saudacao()

    while True:
            # criando a variavel de selecao da opcao premium
            clientePremium = str(input("Deseja ser cliente PREMIUM e ter varios beneficios? [S/N] ")).strip().upper()
            while True:
                if clientePremium not in 'SN':
                    print('Opção Inválida, digite somente S ou N')
                    clientePremium = str(input("Deseja ser cliente PREMIUM e ter varios beneficios? [S/N] ")).strip().upper()
                else:
                    break    
                # condicao caso cliente premium for sim
            if clientePremium in 'S':
                # criando um dicionario vazio
                cliente = {}
                # inserindo os dados na variavel cliente via input
                cliente["nome"] = str(input("Digite seu Nome:"))
                cliente["cpf"] = int(input("Digite seu CPF: "))
                cliente["telefone"] = int(input("Digite Seu Telefone: "))
                cliente["datanasc"] = int(input("Data de Nascimento: "))
                # gravando os dados inseridos no dicionario cliente dentro do arquivo txt
                cadastrarcliente(cliente.copy())
                break
            else:
                #caso a opcao seja não irá direto pro menu
                break
            
menu()            