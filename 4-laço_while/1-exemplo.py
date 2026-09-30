import os
os.system('cls')

while True:
    numero = int(input('digite um numero entre 1 e 10: '))
    if numero < 1 or numero > 10:
        print()# Pular uma linha
        print('numero ivalido tente de novo')
    else:
        print()# Pular uma linha
        print('o numero entre 1 e 10.')
        break #serve para parar o laço de repetiçao assim co /n.

print('= fim =')