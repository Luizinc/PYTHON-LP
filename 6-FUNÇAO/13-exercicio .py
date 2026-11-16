import os
os.system('cls')


def inflacionar_preço(preco_produto):
    if preco_produto >= 100:
        resultado = preco_produto *1.10
    else:
        resultado = preco_produto *1.20

    return resultado

print('= SOLICITANDO VALORES =')
preco_produto = int(input('digite seu preco_produto: '))

resultado = inflacionar_preço(preco_produto)
#CHAMANDO FUNÇAO
preço_inflacionado = inflacionar_preço(preco_produto)

print('= EXIBINDO DADOS =')
print(f'preço inicial: R$ {preco_produto}')
print(f'sua resultado foi de {preço_inflacionado}')