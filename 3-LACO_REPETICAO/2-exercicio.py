import os
os.system('cls')

print('= TABUADA =')
numero = int(input('digite um numero: '))

for i in range(1, 11):
    print('divisao')
    print(f'{numero} / {i} = {numero / i}')
for i in range(1, 11):
    print('multilplicacao')
    print(f'{numero} * {i} = {numero * i}')
for i in range(1, 11):
    print('subtracao')
    print(f'{numero} - {i} = {numero * i}')
for i in range(1, 11):
    print('adiçao')
    print(f'{numero} + {i} = {numero * i}')