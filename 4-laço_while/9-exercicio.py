import os
os.system('cls')

soma_notas = 0
contador = 0

while True:
    nota = float(input('digite sua nota: '))
    soma_notas += nota
    contador += 1

    resposta = input('deseja inserir mais uma nota? (S/N): ').strip().upper()
    if resposta == 'N':
        break
if contador > 0:
    media = soma_notas / contador
    print(f'\nTotal de notas inseridas {contador}')
    print(f'media aritmetica: {media:.2f}')