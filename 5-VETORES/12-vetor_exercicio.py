import os
os.system('cls')

lista_series = []

while True:
    os.system('cls')
    
        
    print('''
=== SENAIFLIX ===
1 - cadastrar serie
2 - listar series
0 - sair
''')
    
    opçao = int(input('escolha uma opçao: '))
    
    match opçao:
        case 1:
            print('\n== CADASTRAR UMA SERIE ==')
            nome = input('nome da serie: ').strip().upper()
            
            if nome == '':
                print('o nome nao pode ficar vazio.')
            elif nome in lista_series:
                print(f'{nome} ja esta cadastrado.')
            else:
                lista_series.append(nome)
                print('serie cadastrado com sucesso!')
            input('Pressione uma tecla para continuar...')

        case 2:
            print('\n== LISTAR TODAS AS SERIES ==')
            if len(lista_series)== 0:
                print('o estoque de series esta vazio')
            else:
                for i, serie in enumerate(lista_series):
                 print(f'{i+1}. {serie}')
            print(f'total de produtos: {len(lista_series)}')
            input('\nPressione uma tecla para continuar...')
            os.system('cls')
            
        case 0:
            print('fim do programa.')
            break
        
        case _:
            print('opçao invalida!')
            input('Pressione uma tecla para continuar...')
        
        