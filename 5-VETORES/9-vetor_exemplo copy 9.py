import os
os.system('cls')

print('= Inserindo notas no vetor =')
vetor_notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input('Digite a nota: '))
    vetor_notas.append(nota)

if nota >= 7:
    print('Aprovado!')
elif nota >=5:
    print('recuperaçao')
else:
    print('reprovado')


# Somar tudo e calcular a média
soma_total = sum(vetor_notas)
media = soma_total / QUANTIDADE_NOTAS

print('\n= Exibindo notas =')
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f'{posicao}ª nota: {nota}')

print(f'\nMédia: {media}')