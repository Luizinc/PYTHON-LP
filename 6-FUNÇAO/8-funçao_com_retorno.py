import os
os.system('cls')

def logo_senai():
    print('='*15)
    print('     SENAI-BAHIA')
    print('='*15)



#funçao com parametros e retorno
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado


print(f'\n= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#usando funçoes co parametros e
#iserindo o retorno na variavel da soma
soma = calcular_notas(nota1, nota2)

print(f'\n= EXIBINDO NOTAS =')
print(f'Soma: {soma}')