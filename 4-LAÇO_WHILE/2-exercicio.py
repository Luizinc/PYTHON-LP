import os
os.system('cls')

while True:
    nota = int(input('digite sua nota: '))
    if nota < 0 or nota > 10:
        print()
        print('/nnota icorreta, digite novamente')
    else:
        print()
        print('nota entre 0 e 10 ')
        print(f'nota: {nota}')
        break
print('= fim =')