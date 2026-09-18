import os
os.system ('cls')

#inicio
altura: float(input('digite sua altura: '))
peso: float(input('digite seu peso: '))

indice=peso/(altura * altura)

#processamento
if imc < 18.5:
    resualtado=print('abaixo do peso')
elif