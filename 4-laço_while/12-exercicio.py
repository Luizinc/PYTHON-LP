import os
os.system('cls')

salarios = []
idades = []
mulheres_salario_alto = 0

while True:
    print("=== PESQUISA DE HABITANTES ===")
    print("1 | Adicionar pessoa")
    print("2 | Exibir resultados")
    print("3 | Sair")
    
    opcao = input("Escolha uma opção: ")
    
    match opcao:
        case "1":
            os.system("cls" if os.name == "nt" else "clear")
            print("--- NOVO CADASTRO ---")
            idade = int(input("Digite a idade: "))
            sexo = input("Digite o sexo (M/F): ").strip().upper()
            salario = float(input("Digite o salário (R$): "))
            
            idades.append(idade)
            salarios.append(salario)
            
            if sexo == "F" and salario >= 5000.00:
                mulheres_salario_alto += 1
                
            print("\nPessoa cadastrada com sucesso!")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls" if os.name == "nt" else "clear")
            
        case "2":
            if len(idades) == 0:
                print("\nNenhum dado foi cadastrado ainda.\n")
            else:
                media_salario = sum(salarios) / len(salarios)
                maior_idade = max(idades)
                menor_idade = min(idades)
                
                print("\n--- RESULTADOS DA PESQUISA ---")
                print(f"a) Média de salário do grupo: R$ {media_salario:.2f}")
                print(f"b) Maior idade: {maior_idade} anos | Menor idade: {menor_idade} anos")
                print(f"c) Mulheres com salário a partir de R$ 5.000,00: {mulheres_salario_alto}\n")
                
        case "3":
            print("\nEncerrando o programa...")
            break
            
        case _:
            print("\nOpção inválida! Tente novamente.\n")