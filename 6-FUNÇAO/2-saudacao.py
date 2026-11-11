import os
os.system('cls')

def mostrar_saudacao(nome, idade):
    print(f'{nome} tem {idade} anos.')

print('= SOLICITANDO DADOS =')
nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

print('\n = EXIBINDO DADOS =')
mostrar_saudacao(nome, idade) #CHAMANDO FUNÇÃO