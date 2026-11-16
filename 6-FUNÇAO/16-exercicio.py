import os

os.system('cls')


def calcular_notas(notas):
    return  sum (lista_notas) / len(lista_notas)



def mostrar_resultado(media, lista_notas):
    print('\n= EXIBINDO NOTAS =')
    for nota in lista_notas:
        print(f'Nota: {nota}')

def status_do_aluno(media):
    if media >= 7:
        resultado = 'aprovado'
    else:
        resultado = 'reprovado'
    return resultado

lista_notas = []

print('= SOLICITANDO NOTAS =')
for i in range(2):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota: '))
        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            break
        else:
            print('Nota invalida, tente novamente! \n')



media = calcular_notas(lista_notas)
status_aluno = status_do_aluno(media)

print('\n= EXIBINDO RESULTADOS =')
mostrar_resultado(media, lista_notas)
print(f'\nMedia: {media}')
print(f'\nSituaçao do aluno: {status_aluno}')

