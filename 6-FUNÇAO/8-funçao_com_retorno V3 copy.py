import os
os.system('cls')

def logo_senai():
    print('='*25)
    print('      SENAI-BAHIA')
    print('='*25)

#funçao com parametros e retorno
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) /2
    return resultado


def verificar_resultado(media):
    if media >= 7:
        resultado = 'aprovado'
    else:
        resultado = 'reprovado'
    return resultado

logo_senai()
print(f'\n= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#usando funçoes co parametros e
#iserindo o retorno na variavel da media
media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)

logo_senai()
print(f'\n= EXIBINDO NOTAS =')
print(f'media: {media}')
print(f'resultado: {situacao}')
