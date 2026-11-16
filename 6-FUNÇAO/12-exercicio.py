import os
os.system('cls')

#funçao com parametro
def conversor_centimetros(metros):
    return  metros*100

print(f'= CONVERSOR DE CENTIMETROS =')
metros = int(input('digite quantos metros quer converter em cm°: '))

converter = conversor_centimetros(metros)
os.system('cls')
print('voce tem {} centimetros'.format(converter))

