import os
os.system('cls')

print('= Inserindo numeros =')
vetor_numero = []

pares = 0
impares = 0

for i in range(6):
    numero = int(input(f'Digite o {i+1}º número: '))
    vetor_numero.append(numero)
    
    # Verifica se é par ou ímpar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1


menor_numero = min(vetor_numero)
maior_numero = max(vetor_numero)

print('\n= Exibindo os números no vetor =')
for posicao, numero in enumerate(vetor_numero, start=1):
    print(f'{posicao}º número: {numero}')

print('\n= EXIBINDO AS ESTATÍSTICAS =')
print(f'Menor número: {menor_numero}')
print(f'Maior número: {maior_numero}')
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')