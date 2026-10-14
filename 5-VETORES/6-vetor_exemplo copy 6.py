import os
os.system('cls')

print('= inseririndo notas no vetor =')
vetor_notas = []

for i in range(3):
    nota = float(input('digite a {i+1}ª nota: '))
    vetor_notas.append(nota)


print('\n= exibindo notas =')
for posiçao, nota in enumerate(vetor_notas, start=1):
    print(f'{posiçao}ª: nota: {nota}')



