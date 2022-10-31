from controller import salvar_itens, salvar_pagamento, ticket

def menu_bomboniere():

    bomboniere = {"Pipoca": 0, "Refrigerante":  0, "Chocolate": 0}

    opcao = "0"
    while opcao != "4":
        print("""
        [ 1 ] = Pipoca
        [ 2 ] = Refrigerante
        [ 3 ] = Chocolate
        [ 4 ] = Sair...
        """)

        opcao = str(input("Escolha uma opção: "))

        match opcao:
            case "1":
                bomboniere["Pipoca"] += int(input("\nInforme a quantidade: "))
            case "2":
                bomboniere["Refrigerante"] += int(input("\nInforme a quantidade: "))
            case "3":
                bomboniere["Chocolate"] += int(input("\nInforme a quantidade: "))
            case "4":
                print("\nFinalizando a bomboniere.")
            case _:
                print("\nOpção inválida.")

    salvar_itens(bomboniere)


def menu_pagamento():

    forma_pagamento = {}

    print("""
    [ 1 ] = Dinheiro
    [ 2 ] = Cartão
    [ 3 ] = Pix
    """)

    opcao = str(input("Escolha uma opção: "))

    match opcao:
        case "1":
            forma_pagamento["Pagamento"] = "Dinheiro"
        case "2":
            forma_pagamento["Pagamento"] = "Cartão"
        case "3":
            forma_pagamento["Pagamento"] = "Pix"
        case _:
            print("\nOpção inválida.")

    salvar_pagamento(forma_pagamento)


#menu_bomboniere()
#menu_pagamento()
ticket()