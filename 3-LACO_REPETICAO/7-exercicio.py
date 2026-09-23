import os
os.system('cls')

soma=0

for i in range(5):

    numero = int(input(f'digite o {i+1}º numero inteiro: '))

    soma += numero


print(f'a soma de todos os numeros lidos e {soma}')
