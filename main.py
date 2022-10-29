bomboniere = {}

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
            bomboniere["Pipoca"] = str(input("Informe a quantidade: "))
        case "2":
            bomboniere["Refrigerante"] = str(input("Informe a quantidade: "))
        case "3":
            bomboniere["Chocolate"] = str(input("Informe a quantidade: "))
        case "4":
            print("Finalizando a bomboniere.")
        case _:
            print("Opção inválida.")

print(bomboniere)






