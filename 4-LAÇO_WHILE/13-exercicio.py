import os
os.system('cls')

salarios = []
filhos = []

while True:
    print("=== PESQUISA DA PREFEITURA ===")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    
    opcao = input("Escolha uma opção: ")
    
    match opcao:
        case "1":
            salario = float(input("Digite o salário da família (R$): "))
            qtd_filhos = int(input("Digite o número de filhos: "))
            
            salarios.append(salario)
            filhos.append(qtd_filhos)
            print("Família adicionada com sucesso!\n")
            
        case "2":
            total_familias = len(salarios)
            if total_familias == 0:
                print("\nNenhuma família foi cadastrada.")
            else:
                media_salario = sum(salarios) / total_familias
                media_filhos = sum(filhos) / total_familias
                maior_salario = max(salarios)
                menor_salario = min(salarios)
                
                print("\n=== RESULTADOS FINAIS ===")
                print(f"a) Total de famílias que responderam: {total_familias}")
                print(f"b) Média do salário da população: R$ {media_salario:.2f}")
                print(f"c) Média do número de filhos: {media_filhos:.2f}")
                print(f"d) Maior salário: R$ {maior_salario:.2f}")
                print(f"e) Menor salário: R$ {menor_salario:.2f}")
            break
            
        case _:
            print("Opção inválida! Tente novamente.\n")