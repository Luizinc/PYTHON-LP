import os
os.system('cls')


def calculando_media(notas):
    media = sum(notas) / len(notas)
    return media


vetor_notas = []


for i in range (3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)

media_final = calculando_media(vetor_notas)

print(f"Média: {media_final}")