import os
os.system('cls')

def multiplacador_notas(nota1,nota2):
    notas = nota1 * nota2
    return notas

nota1 = int(input('digite sua nota: '))
nota2 = int(input('digite sua nota: '))

resultado = multiplacador_notas(nota1,nota2)


print(f'sua nota multiplicada e {resultado}')