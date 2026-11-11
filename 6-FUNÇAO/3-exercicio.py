import os
os.system('cls')

def logo_senai ():
    print('\n')
    print('='* 15)
    print('  SENAI-BAHIA')
    print('='* 15)

def mostrar_dados(nome,email,telefone):
    print(f'{nome} seu e email {email} e o seu {telefone}.')
logo_senai()




nome = input('digite seu nome: ')
email = input('digite seu email: ')
telefone = input('digite seu telefone: ')
os.system('cls')

logo_senai()
mostrar_dados(nome,email,telefone) #CHAMANDO FUNÇÃO