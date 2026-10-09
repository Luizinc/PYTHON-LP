import os
os.system('cls')

soma = 0
quantidade = 0

while True:
    valor= int(input('digite um valor inteiro positivo: '))
    if valor < 0:
        break
    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f'nMedia aritmetica dos numeros informados: {media:.2f}')
else:
    print('nenhum numero positivo foi digitado.')