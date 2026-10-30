import os

lista_jogadores = []

while True:
    os.system('cls')

    print('''
=== GESTAO DE JOGADORES ===
1- Cadastrar jogador
2- Listar todos os jogadores
3- Atualizar jogador
4- Remover jogador
5- Buscar jogador
0- Sair
''')

    opcao = int(input('escolha a opcao: '))

    match opcao:
        case 1:
            # CREATE (INSERIR)
            print('== CADASTRAR JOGADOR ==')
            nome = input('digite o nome do jogador: ').strip().upper()
            posicao = input('digite a posicao do jogador: ').strip().upper()
            camisa = input('digite o numero da camisa: ').strip()

            if nome == '' or posicao == '' or camisa == '':
                print('todos os campos devem ser preenchidos...')
            else:
                # Verifica se a camisa ja esta cadastrada em algum jogador
                camisa_usada = False
                for jogador in lista_jogadores:
                    if f'#{camisa}' in jogador:
                        camisa_usada = True

                if camisa_usada:
                    print('erro: numero de camisa ja cadastrado!')
                else:
                    jogador = f"{nome} | {posicao} | #{camisa}"
                    lista_jogadores.append(jogador)
                    print('jogador cadastrado com sucesso!')

        case 2:
            # READ (LISTAR TODOS)
            print('== ELENCO DE JOGADORES ==')
            if len(lista_jogadores) == 0:
                print('o elenco esta vazio.')
            else:
                for jogador in lista_jogadores:
                    print('-', jogador)
                print(f'Total: {len(lista_jogadores)}')

        case 3:
            # UPDATE (ATUALIZAR)
            print('== ATUALIZAR JOGADOR ==')
            busca = input('digite o nome do jogador que deseja atualizar: ').strip().upper()
            
            encontrado = ''
            for jogador in lista_jogadores:
                if busca in jogador:
                    encontrado = jogador

            if encontrado in lista_jogadores and encontrado != '':
                posicao = lista_jogadores.index(encontrado)
                
                novo_nome = input('novo nome: ').strip().upper()
                nova_posicao = input('nova posicao: ').strip().upper()
                nova_camisa = input('nova camisa: ').strip()

                if novo_nome == '' or nova_posicao == '' or nova_camisa == '':
                    print('os campos nao podem ser em branco.')
                else:
                    # Verifica se a nova camisa ja existe em outro jogador
                    camisa_usada = False
                    for j in lista_jogadores:
                        if f'#{nova_camisa}' in j and j != encontrado:
                            camisa_usada = True

                    if camisa_usada:
                        print('erro: essa camisa ja esta em uso por outro jogador!')
                    else:
                        lista_jogadores[posicao] = f"{novo_nome} | {nova_posicao} | #{nova_camisa}"
                        print('jogador alterado com sucesso!')
            else:
                print('jogador nao encontrado.')

        case 4:
            # DELETE (REMOVER)
            print('\n== REMOVER JOGADOR ==')
            busca = input('digite o nome do jogador que deseja remover: ').strip().upper()
            
            encontrado = ''
            for jogador in lista_jogadores:
                if busca in jogador:
                    encontrado = jogador

            if encontrado in lista_jogadores and encontrado != '':
                lista_jogadores.remove(encontrado)
                print('jogador excluido com sucesso!')
            else:
                print('jogador nao encontrado.')

        case 5:
            # READ (BUSCAR/FILTRAR)
            print('\n== ENCONTRAR JOGADOR ==')
            busca = input('digite o nome, posicao ou camisa para buscar: ').strip().upper()
            
            achou = False
            for jogador in lista_jogadores:
                if busca in jogador:
                    print('encontrado:', jogador)
                    achou = True
            
            if not achou:
                print('nenhum jogador encontrado.')

        case 0:
            print('saindo do programa...')
            break

        case _:
            print('opcao invalida! \nTente novamente...')

    input('pressione uma tecla para continuar...')