import os
os.system('cls')

def calculo_soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def calculo_subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def calculo_multiplcacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def calculo_divisao(numero1, numero2):
    if numero2 == 0:
        print('Atençao e zero!')
    resultado = numero1 / numero2
    return resultado

print(f'= RECEBENDO NUMEROS =')
numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))

resultado_soma = calculo_soma(numero1, numero2)
resultado_subtracao = calculo_subtracao(numero1, numero2)
resultado_multiplicacao = calculo_multiplcacao(numero1, numero2)
resultado_divisao = calculo_divisao(numero1, numero2)

print(f'= RESULTADO =')
print(resultado_soma)
print(resultado_subtracao)
print(resultado_multiplicacao)
print(resultado_divisao)

