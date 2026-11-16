import os

os.system('cls')


def calcular_notas(notas):
    media = sum(notas) / len(notas)
    return media


def mostrar_resultado(media, lista_notas):
    print('\n= EXIBINDO NOTAS =')
    for nota in lista_notas:
        print(f'Nota: {nota}')
    print(f'Média: {media:.2f}')


lista_notas = []

for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)

media = calcular_notas(lista_notas)
mostrar_resultado(media, lista_notas)
