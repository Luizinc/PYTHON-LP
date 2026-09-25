import os
os.system('cls')

print('ACUMULANDO VALORES DE UMA VARIAVEL.')
soma = 0

print(f'valor INICIAL da variavel soma: {soma}')

print(f'valor INICIAL da variavel soma: {soma}')

for i in range(3):
    numero = int(input('digite um numero para somar: '))
    soma = soma + numero
    print(f'valor TEMPORARIO da variavel soma: {soma}')

print(f'/nValor FINAL da variavel soma: {soma}')
