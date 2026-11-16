import os
from datetime import date

os.system('cls')

def solicitando_idade(data):
    ano_atual = date.today().year
    resultado = ano_atual - data
    return resultado

print('= SOLICITANDO DATA =')
data = int(input('digite seu ano de nascimento: '))

idade = solicitando_idade(data)

print(f'Sua idade e {idade}')