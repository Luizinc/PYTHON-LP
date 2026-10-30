#CRUD

import os

lista_produtos = []

while True:
    os.system('cls')

    print('''
=== MERCADINHO DENDEZEIROS ===
1- cadastrar produto
2- Listar todos os produtos
3- atualizar produto
4- remover produto
5- buscar produto
0- sair
''')

    opçao = int(input('escolha a opçao: '))

    match opçao:
        case 1:
            #CREATE (INSERIR)
            print('== CADASTRAR PRODUTO ==')
            nome_produto = input('digite o nome do novo produto: ').strip().upper()
            if nome_produto == '':
                print('o nome do produto deve ser inserido...')
            elif nome_produto in lista_produtos:
                print('produto ja cadastrado.')
            else:
                lista_produtos.append(nome_produto)
                print('produto cadstrado com sucesso!')

        case 2:
            #READ (LER/BUSCAR)
            print('== PRODUTOS NO ESTOQUE ==')
            for produto in lista_produtos:
                print('-', produto)
            print(f'Total: {len(lista_produtos)}')

        case 3:
            #UPDATE (ATUALIZAR)
            print('== ATUALIZAR PRODUTOS ==')
            nome = input('Qual produto deseja atualizar?')
            if nome in lista_produtos:
                posiçao = lista_produtos.index(nome)
                novo = input('novo nome: ')
                lista_produtos[posiçao] = novo
                print('produto alterado com sucesso!')

        case 4:
            #DELETE (REMOVER)
            print('\n== REMOVER PRODUTO ==')
            nome = input('qual produto deseja remover? ')
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('produto excluido com sucesso!')
            else:
                print('produto nao encontrado')

        case 5:
            #READ (LER/FILTRAR/BUSCAR)
            print('\n== ENCONTRAR PRODUTO ==')
            nome = input('qual produto deseja buscar? ')
            if nome in lista_produtos:
                print('produto encontrado com sucesso!')
            else:
                print('este produto nao esta no estoque.')
            
        case 0:
            print('saindo do programa...')
            break
        case _:
            print('opçao invalida! \nTente novamente...')
    input('pressione uma tecla para continuar...')