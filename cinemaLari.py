import os

while True:
    # Aqui vem o menu com as opções de filmes, e uma validação caso não foi selecionado uma as opções válidas.
    filme = input("Qual filme você gostaria de assistir hoje? \n1- Matrix; \n2- Star Wars IV - Uma Nova Esperança; \n3- Clube da Luta; \n4- Harry Potter e o Prisioneiro de Azkaban; \n5- Top Gun - Maverick; \n\n:> ")
    while True:
        if filme not in ("12345"): # temos opção de filme de 1 à 5, então tudo que for diferente vai voltar a opção para reavaliar.
            print("\nEscolha um dos filmes em cartaz. \n")
            filme = input("Qual filme você gostaria de assistir hoje? \n1- Matrix; \n2- Star Wars IV - Uma Nova Esperança; \n3- Clube da Luta; \n4- Harry Potter e o Prisioneiro de Azkaban; \n5- Top Gun - Maverick; \n\n:> ")
        else:
            break
    os.system("cls")    
    #precisa colocar aqui para ele salvar na função no controller

    #ofertar as opções de poltronas dentro de uma lista, e se possível - deve-se eliminar a opção selecionada pelo anterior.
    listaPoltronas = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5"]
    print(f"Escolha uma das poltronas disponíveis na lista {listaPoltronas}")
    escolhaPoltrona = input("\n>: ").upper()
    #Aqui deve-se colocar uma validação para caso não selecionar uma das opções.
    while True:
        if escolhaPoltrona not in listaPoltronas:
            print("\nEscolha uma das opções oferecidas.")
            print(f"\nEscolha uma das poltronas disponíveis na lista {listaPoltronas}")
            escolhaPoltrona = input("\n>: ").upper()
        else:
            break
    os.system("cls")
    # Precisa colocar aqui para ele salvar na função do controller.
    # Aqui abre a opção se quer algo do bomboniere. 
    input("Você gostaria de algum item de bomboniere? \n1- Sim; \n2- Não; \n\n:> ")