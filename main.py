# Importa as funçôes da controller
from controller import salvar_itens, salvar_pagamento, ticket, limpaarquivo

# Funcao do Menu Bomboniere
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

    # Chama a função para salvar os itens digitados via Input no Dicionário
    salvar_itens(bomboniere)


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

limpaarquivo()

menu_bomboniere()

menu_pagamento()

ticket()