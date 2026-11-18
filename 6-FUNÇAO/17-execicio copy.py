import os
os.system('cls')

def convertendo_massa (peso, altura):
    imc = peso/(altura * altura)
    if imc < 18.5:
        resultado = 'abaixo do peso \nconsulte um nutricionista para orientaçao.'
    elif  imc < 25:
        resultado = 'peso normal \nmatenha habitos saudaveis'
    elif imc < 30:
        resultado = 'sobrepeso \nconsidere uma dieta balanceada e atividade fisica'
    elif imc < 35:
        resultado = 'obesidade grau 1 \nprocure orientaçao de um profissional de saude'
    elif imc < 40:
        resultado = 'obesidade grau 2 \nprocure um medico para avaliaçao e orientaçao'
    else:
        resultado = 'obesidade grau 3 \nbusque assistencia medica imediatamente'          
    return imc, resultado

    
print('\n= RECEBENDO DADOS =')
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

#chamando a funçao
indice_corporal, menssagem = convertendo_massa(peso,altura)

os.system('cls')

print('\n= RESULTADO =')
print(f'seu indice corporal e {indice_corporal:.2f}')
print(menssagem)
