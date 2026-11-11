import os
os.system('cls')

def mostrar_tabuada(numero):
    for i in range(1,10):
        print(f'{numero} x {i} = {numero*i}')
    
print('= SOLICITANDO DADOS')
numero = int(input('digite um numero para tabuada: '))

print('\n= EXIBINDO DADOS =')
mostrar_tabuada(numero)
