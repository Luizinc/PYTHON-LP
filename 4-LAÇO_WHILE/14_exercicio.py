import os
os.system('cls')

soma_salario = total = mulheres5k = maior_idade = 0
menor_idade = 999
opcao = 0

while opcao != 3:
    print('1 | add pessoa\n2 | resultado\n3 | sair')
    opcao= int(input('opcao: '))

    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear' )

        idade = int(input('idade: '))
        sexo = input('sexo (M/F): ').upper()
        salario = float(input('salario: R$ '))

        total += 1
        soma_salario += salario
        maior_idade = max(maior_idade,idade)
        menor_idade = min(menor_idade,idade)


        if sexo == 'F' and salario >= 5000:
            mulheres5k += 1
            

        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao ==2:

        if total > 0:
            print(f"\na) Média: R$ {soma_salario / total:.2f}")
            print(f"b) Maior: {maior_idade} | Menor: {menor_idade}")
            print(f"c) Mulheres >= R$5k: {mulheres5k}\n")
        else:
            print("\nNenhum dado cadastrado ainda.\n")