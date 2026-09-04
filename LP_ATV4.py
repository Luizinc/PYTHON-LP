import os
os.system('cls')

nota= float(input('digite sua nota: '))

if nota >=0.0 and nota <=10.0:
    print(f'nota valida: {nota}')
else:
    print('nota inavlida! tem que ser de zero a dez:')