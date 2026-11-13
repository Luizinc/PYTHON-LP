import os
os.system('cls')

#sem parametros
def logo_senai():
    print('='*15)
    print('     SENAI')
    print('='*15)


#com parametros
def mostar_dados(nome, idade):
    print(f'{nome} tem {idade} anos.')
#funçao sem retorno
logo_senai()
nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

logo_senai()
print('\n= EXIBINDO DADOS =')
mostar_dados(nome,idade)