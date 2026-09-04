import os
os.system('cls')

#solicitando dados
media=float(input('digite a nota1: '))
media=float(input('digite a nota2: '))
faltas=int(input('quantas faltas: '))



if media >= 7.0 and faltas <= 40:
    print('parabens voce foi aprovado')
else:
    print('reprovado')    