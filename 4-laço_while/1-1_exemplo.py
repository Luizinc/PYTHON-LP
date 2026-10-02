import os
os.system('cls')

while True:
    print('''
        = MENU =
opção       produto         preço
1           macarrão        R$ 3.80
2           uvas            R$ 7.00
3           arroz           R$ 5.50
4           feijão          R$ 8.00
5           suco            R$ 4.00
0           sair
''')

    opcao = input("Digite qual produto deseja (ou 0 para sair): ").strip()

    match opcao:
        case "1":
            print("\n-> Opção escolhida: macarrão")
            print("-> Preço: R$ 3.80")
        case "2":
            print("\n-> Opção escolhida: uvas")
            print("-> Preço: R$ 7.00")
        case "3":
            print("\n-> Opção escolhida: arroz")
            print("-> Preço: R$ 5.50")
        case "4":
            print("\n-> Opção escolhida: feijão")
            print("-> Preço: R$ 8.00")
        case "5":
            print("\n-> Opção escolhida: suco")
            print("-> Preço: R$ 4.00")
        case "0":
            print("\nSaindo do programa. Até logo!")
            break  # Encerra o loop while
        case _:
            print("\n[ERRO] Opção inválida! Escolha de 1 a 5 ou 0 para sair.")
        
    input("\nPressione Enter para voltar ao menu...")
    os.system('cls')
