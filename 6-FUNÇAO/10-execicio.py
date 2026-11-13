import os
os.system('cls')

def verfifacar_numero (numero):
    if numero >0:
        resultado = 'positivo'
    elif numero ==0:
        resultado = 'neuto'
    else:
        resultado = 'negativo'
    return resultado

print(f'= PEDINDO NUMERO =')
numero = int(input('digite um numero: '))
resultado = verfifacar_numero(numero)

os.system('cls')

print(f'= EXIBINDO RESULTADO =')
print(f'o numero {numero} é {resultado}')