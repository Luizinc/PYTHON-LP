import os
os.system('cls')

print('= inseririndo notas no vetor =')
vetor_notas = []
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    nota = float(input('digite a {i+1}ª nota: '))
    vetor_notas.append(nota)

#Sun - somar tudo que esta no vetor.
soma = sum(vetor_notas) / QUANTIDADE_NOTAS

print('\n= exibindo notas =')
for posiçao, nota in enumerate(vetor_notas, start=1):
    print(f'{posiçao}ª: nota: {nota}')

print(f'media: {soma}')

