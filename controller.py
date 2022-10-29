from datetime import datetime

def saudacao():
    
    hora = datetime.today().strftime('%H:%M')
    saudacao = ''

    if hora > ('06:00') and hora < ('12:00'):
        saudacao = 'Bom dia!'
    elif hora > ('12:00') and hora < ('18:00'):
        saudacao = 'Boa tarde!'
    else: 
        saudacao = 'Boa noite!'

    print(hora, '\n')
    print('Boa Noite! Seja bem vindo ao Cinema Pytrix\n'.format(saudacao))    

def cadastrarcliente(cliente):
    with open('cadastrosPremium.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+'\n')
