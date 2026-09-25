import os
os.system('cls')

QUANTIDADE = 5
impares = 0
pares= 0
soma=0

for i in range(5):

    soma += int(input(f'digite o {i+1}º numero inteiro: '))

for i in range(QUANTIDADE):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        pares = pares + 1
        pares += 1
    else:
        impares = impares + 1

print(f'quantidade de pares {pares}')
print(f'quantidade de pares {impares}')



print(f'a soma de todos os numeros lidos e {soma}')
