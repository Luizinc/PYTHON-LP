import os
os.system('cls')

def logo_senai():
    print('='*25)
    print('      SENAI-BAHIA')
    print('='*25)

logo_senai()
def calculo_pares(numero):
    if numero % 2==0:
        resultado = 'par'
    else:
        resultado ='impar'
    return resultado

os.system('cls')

logo_senai()
print(f'\n= PEDINDO NUMEROS =')
numero = int(input('digite um numero: '))
resultado = calculo_pares(numero)
os.system('cls')
print('\n = EXIBINDO RESULTADOS =')
print(f'o numero {numero} é {resultado}')