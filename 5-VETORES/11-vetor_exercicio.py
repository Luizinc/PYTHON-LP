import os
os.system('cls')

lista_produtos = []

while True:
    os.system('cls')
    
        
    print('''
=== MERCADINHO DENDEZEIROS ===
1 - cadastrar produtos
2 - listar produtos
0 - sair
''')
    
    opçao = int(input('escolha uma opçao: '))
    
    match opçao:
        case 1:
            print('\n== CADASTRAR UM PRODUTO ==')
            nome = input('nome do novo produto: ').strip().upper()
            
            if nome == '':
                print('o nome nao pode ficar vazio.')
            elif nome in lista_produtos:
             print(f'{nome} ja esta cadastrado.')
            else:
              lista_produtos.append(nome)
              print('produto cadastrado com sucesso!')
              input('Pressione uma tecla para continuar...')
              
        case 2:
            print('\n== LISTAR TODOS OS PRODUTOS ==')
            if len(lista_produtos)== 0:
                print('o estoque esta vazio')
            else:
             for i, produto in enumerate(lista_produtos):
                print(f'{i+1}. {produto}')
            print(f'total de produtos: {len(lista_produtos)}')
            input('\nPressione uma tecla para continuar...')
            os.system('cls')
            
        case 0:
            print('fim do programa.')
            break
        
        case _:
            print('opçao invalida!')
            input('Pressione uma tecla para continuar...')
        
        