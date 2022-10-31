# importando biblioteca
import os
# importando as funcoes
from controller import saudacao, cadastrarcliente, salvar_itens, salvar_pagamento, ticket, salvarfilme, salvarpoltrona,limparticket

# Função Menu Forma de menuPremium
def menuPremium():
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
                os.system("cls")
                break
            else:
                #caso a opcao seja não irá direto pro menu
                os.system("cls")
                break

# Função Menu Filme
def menufilme():
    while True:
        filmes = {}
        # Aqui vem o menu com as opções de filmes, e uma validação caso não foi selecionado uma as opções válidas.
        filme = input("Qual filme você gostaria de assistir hoje? \n1- Matrix; \n2- Star Wars IV - Uma Nova Esperança; \n3- Clube da Luta; \n4- Harry Potter e o Prisioneiro de Azkaban; \n5- Top Gun - Maverick; \n\n:> ")
        match filme:
            # Se opção for 1
            case "1":
                filmes["Filme"] = "Matrix"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 2
            case "2":
                filmes["Filme"] = "Star Wars IV - Uma Nova Esperança"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 3
            case "3":
                filmes["Filme"] = "Clube da Luta"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 4        
            case "4":
                filmes["Filme"] = "Harry Potter e o Prisioneiro de Azkaban"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 5
            case "5":
                filmes["Filme"] = "Top Gun - Maverick"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for inválida
            case _:
                print("\nOpção inválida.")
                print("\nEscolha um dos filmes em cartaz. \n")
        
        
        os.system("cls")    
    
# Função Menu Forma de Poltrona    
def menupoltrona():
        #ofertar as opções de poltronas dentro de uma lista, e se possível - deve-se eliminar a opção selecionada pelo anterior.
        listaPoltronas = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5"]
        print(f"Escolha uma das poltronas disponíveis na lista {listaPoltronas}")

        #Aqui deve-se colocar uma validação para caso não selecionar uma das opções.
        while True:
            posicaoPoltrona = {}

            posicaoPoltrona["Poltrona"] = input("\n>: ").upper()
            
            while True:
                if posicaoPoltrona["Poltrona"] not in listaPoltronas:
                    print("\nEscolha uma das opções oferecidas.")
                    print(f"\nEscolha uma das poltronas disponíveis na lista {listaPoltronas}")
                    posicaoPoltrona["Poltrona"] = input("\n>: ").upper()
                    salvarpoltrona(posicaoPoltrona)

                else:
                    salvarpoltrona(posicaoPoltrona)
                    break
            break    

        os.system("cls")


# Função Menu Forma de Bomboniere
def menu_bomboniere():
            # Cria um Dicionário para a Bomboniere
            bomboniere = {"Pipoca": 0, "Refrigerante": 0, "Chocolate": 0}

            # Cria uma variável para referencia ao While
            opcao = "0"

            # Cria uma estrutura de repetição para o Menu Bomboniere
            while opcao != "4":
                print("""
                [ 1 ] = Pipoca
                [ 2 ] = Refrigerante
                [ 3 ] = Chocolate
                [ 4 ] = Sair...
                """)

                # Variável recebe a opção do Menu
                opcao = str(input("Escolha uma opção: "))

                # Switch com as opções da Bomboniere
                match opcao:
                    # Se opção for 1
                    case "1":
                        # Inserindo ou incrementa no Dicionário
                        bomboniere["Pipoca"] += int(input("\nInforme a quantidade: "))
                    # Se opção for 2
                    case "2":
                        # Inserindo ou incrementa no Dicionário
                        bomboniere["Refrigerante"] += int(input("\nInforme a quantidade: "))
                    # Se opção for 3
                    case "3":
                        # Inserindo ou incrementa no Dicionário
                        bomboniere["Chocolate"] += int(input("\nInforme a quantidade: "))
                    # Se opção for 4
                    case "4":
                        # Sai do menu
                        print("\nFinalizando a bomboniere.")
                    # Se opção for válida
                    case _:
                        # Informa opção inválida
                        print("\nOpção inválida.")

# Função Menu Forma de Pagamento
def menu_pagamento():


    # Cria o um Dicionário para forma de pagamento
    forma_pagamento = {}

    # Cria uma estrutura de repetição para o Menu Forma de Pagamento
    while True:
        print("""
        [ 1 ] = Dinheiro
        [ 2 ] = Cartão
        [ 3 ] = Pix
        """)

        # Variável recebe a opção do Menu forma de PagaMENTO
        opcao = str(input("Escolha uma opção: "))

        # Switch com as opções da Bomboniere
        match opcao:
            # Se opção for 1
            case "1":
                forma_pagamento["Pagamento"] = "Dinheiro"
                # Chama a função para salvar no Dicionário
                salvar_pagamento(forma_pagamento)
                # Break para sair do Menu
                break
            # Se opção for 2
            case "2":
                forma_pagamento["Pagamento"] = "Cartão"
                # Chama a função para salvar no Dicionário
                salvar_pagamento(forma_pagamento)
                # Break para sair do Menu
                break
            # Se opção for 3
            case "3":
                forma_pagamento["Pagamento"] = "Pix"
                # Chama a função para salvar no Dicionário
                salvar_pagamento(forma_pagamento)
                # Break para sair do Menu
                break
            # Se opção for inválida
            case _:
                print("\nOpção inválida.")


#Programa principal
#Chamando as funções
limparticket()
menuPremium()       
menufilme()
menupoltrona()
# Aqui abre a opção se quer algo do bomboniere. 
bombonieri = input("Você gostaria de algum item de bomboniere? \n1- Sim; \n2- Não; \n:> ") 
if bombonieri in '1':
    menu_bomboniere()
menu_pagamento()
ticket()   
