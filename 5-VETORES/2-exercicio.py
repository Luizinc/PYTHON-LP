import os
os.system('cls')

vetor_nomes = []


for i in range(3):
    nomes = input('digite seu nome: ')
# inserindo a nota no vetor de notas.
    vetor_nomes.append(nomes)

for i in range(3):
    print(f'nomes: {vetor_nomes[i]}')