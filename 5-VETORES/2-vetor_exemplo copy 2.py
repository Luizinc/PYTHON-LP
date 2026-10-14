import os
os.system('cls')

print('= inseririndo numeros no vetor =')
vetor_numeros = []

for i in range(3):
    numero = int(input('digite um numero: '))
    vetor_numeros.append(numero)


print('\n= exibindo dados so vetor =')
for index in range(3):
    print(f'valores: {vetor_numeros[index]}')
    print(f'valores: {vetor_numeros[index]}')


