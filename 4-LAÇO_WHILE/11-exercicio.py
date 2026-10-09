import os
os.system('cls')

qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0
qtd_total = 0

while True:
    numero = int(input('digite um numero inteiro positivo: '))

    if numero == 0:
        break

    if numero < 0:
        print('por favor, apenas numeros inteiros!.')

    soma_geral += numero
    qtd_total += 1

    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    else:
        qtd_impares += 1

print('\n=== RESULTADOS ===')
print(f'a) quantidade de numeros pares: {qtd_pares}')
print(f"   Quantidade de números ímpares: {qtd_impares}")

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"b) Média dos valores pares: {media_pares:.2f}")
else:
    print("b) Média dos valores pares: Nenhum número par foi informado.")

if qtd_total > 0:
    media_geral = soma_geral / qtd_total
    print(f"c) Média geral dos números lidos: {media_geral:.2f}")
else:
    print("c) Média geral: Nenhum número foi informado.")