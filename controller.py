#importando as bibliotecas
from datetime import datetime
from time import sleep
#criando a funcao saudação
def saudacao():
    
    # criando uma variavel recebendo a hora atual
    hora = datetime.today().strftime('%H:%M')
    saudacao = ''
    # condicao de verificao da saudacao do dia
    if hora > ('06:00') and hora < ('12:00'):
        saudacao = 'Bom dia!'
    elif hora > ('12:00') and hora < ('18:00'):
        saudacao = 'Boa tarde!'
    else: 
        saudacao = 'Boa noite!'

    # printando a hora e saudação
    print(hora, '\n')
    print('Boa Noite! Seja bem vindo ao Cinema Pytrix\n'.format(saudacao))    

    # funcao de  salvar o cliente no arquivo txt
def cadastrarcliente(cliente):
    with open('cadastrosPremium.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+'\n')

