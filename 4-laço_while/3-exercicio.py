import os
os.system('cls')

nota_total = 0
quantidade_notas = 2
contador = 0

# WHILE EXTERNO: Controla a quantidade de notas
while contador < quantidade_notas:
    
    # Criamos a variável com um valor inválido (-1) para GARANTIR que o while interno comece
    nota = -1
    
    # WHILE INTERNO: Repete ENQUANTO a nota for menor que 0 OU maior que 10
    # Nota: Para o "and", podemos inverter a lógica criando uma flag ou limpando a condição
    while nota < 0 or nota > 10:
        nota = float(input(f'Digite a nota {contador + 1} (entre 0 e 10): '))
        
        # Aqui usamos o AND: Se a nota NÃO estiver entre 0 E 10, avisa o erro
        if not (nota >= 0 and nota <= 10):
            print('\nNota incorreta, digite novamente.\n')

    print(f'Nota {nota} aceita com sucesso!\n')
    nota_total += nota
    contador += 1

media = nota_total / quantidade_notas
print(f'A média final é: {media}')
