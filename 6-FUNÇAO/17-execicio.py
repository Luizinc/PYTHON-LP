import os
os.system('cls')

def convertendo_massa (peso, altura):
    imc = peso/(altura * altura)
    if imc < 18.5:
        print('abaixo do peso')
        print('consulte um nutricionista para orientaçao.')
    elif  imc < 25:
        print('peso normal')
        print('matenha habitos saudaveis')
    elif imc < 30:
        print('sobrepeso')
        print('considere uma dieta balanceada e atividade fisica')
    elif imc < 35:
        print('obesidade grau 1')
        print('procure orientaçao de um profissional de saude')
    elif imc < 40:
        print('obesidade grau 2')
        print('procure um medico para avaliaçao e orientaçao')
    else:
        print('obesidade grau 3')
        print('busque assistencia medica imediatamente')            
    return imc

    
print('\n= RECEBENDO DADOS =')
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

indice_corporal = convertendo_massa(peso,altura)

print(f'seu indice corporal e {indice_corporal:.2f}')
