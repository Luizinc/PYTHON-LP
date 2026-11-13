import os
os.system('cls')

def calculo_soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado_soma

def calculo_subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado_subtracao

def calculo_multiplcacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado_multiplicacao

def calculo_divisao(numero1, numero2):
    if numero2 == 0:
        print('Atençao e zero!')
    resultado = numero1 / numero2
    return resultado_divisao

print(f'= RECEBENDO NUMEROS =')
numero1 = float(input('digite um numero: '))
numero2 = float(input('digite um numero: '))

print(f'= RESULTADO =')
resultado_soma = calculo_soma(numero1, numero2)
resultado_subtracao = calculo_subtracao(numero1, numero2)
resultado_multiplicacao = calculo_multiplcacao(numero1, numero2)
resultado_divisao = calculo_divisao(numero1, numero2)

print({resultado_soma})
print({resultado_subtracao})
print({resultado_multiplicacao})
print({resultado_divisao})



