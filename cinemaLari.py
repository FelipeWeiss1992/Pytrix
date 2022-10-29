while True:
    filme = input("Qual filme você gostaria de assistir hoje? \n1- Matrix; \n2- Star Wars IV - Uma Nova Esperança; \n3- Clube da Luta; \n4- Harry Potter e o Prisioneiro de Azkaban; \n5- Top Gun - Maverick; \n:> ")
    #precisa colocar aqui para ele salvar na função no controller

    listaPoltronas = ("A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5")
    print(f"Escolha uma das poltronas disponíveis na lista {listaPoltronas}")
    escolhaPoltrona = input(">: ")
    if escolhaPoltrona not in listaPoltronas ("A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5"):
        print("Escolha uma das opções oferecidas.")
    else:
        input("Você gostaria de algum item de bomboniere? \n")