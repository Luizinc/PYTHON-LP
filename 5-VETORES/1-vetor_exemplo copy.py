import os
os.system('cls')

print('= inseririndo numeros no vetor =')
vetor_numeros = []

numero = int(input('digite um numero: '))
vetor_numeros.append(numero)
numero = int(input('digite um numero: '))
vetor_numeros.append(numero)
numero = int(input('digite um numero: '))
vetor_numeros.append(numero)

print('\n= exibindo dados so vetor =')
print(f'primeira posiçao do vetor: {vetor_numeros[0]}')
print(f'ultima posiçao do vetor: {vetor_numeros[2]}')


