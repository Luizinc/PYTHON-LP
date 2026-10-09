import os
os.system('cls')

vetor_notas = []


for i in range(3):
    nota = float(input('digite sua nota: '))
    vetor_notas.append(nota) # inserindo a nota no vetor de notas.

for i in range(3):
    print(f'nota: {vetor_notas[i]}')