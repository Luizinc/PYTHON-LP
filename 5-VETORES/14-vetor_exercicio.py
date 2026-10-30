import os

lista_pacientes = []

while True:
    os.system('cls')

    print('''
=== SISTEMA DE PACIENTES ===
1- Cadastrar paciente
2- Listar todos os pacientes
3- Atualizar paciente
4- Remover paciente
5- Buscar paciente
0- Sair
''')

    opcao = int(input('escolha a opcao: '))

    match opcao:
        case 1:
            print('== CADASTRAR PACIENTE ==')
            nome = input('digite o nome do paciente: ').strip().upper()
            sobrenome = input('digite o sobrenome do paciente: ').strip().upper()

            if nome == '' or sobrenome == '':
                print('o nome e o sobrenome devem ser inseridos...')
            else:
                paciente = nome + ' ' + sobrenome
                if paciente in lista_pacientes:
                    print('paciente ja cadastrado.')
                else:
                    lista_pacientes.append(paciente)
                    print('paciente cadastrado com sucesso!')

        case 2:
            print('== LISTA DE PACIENTES ==')
            for paciente in lista_pacientes:
                print('-', paciente)
            print(f'Total: {len(lista_pacientes)}')

        case 3:
            print('== ATUALIZAR PACIENTE ==')
            nome = input('Qual paciente deseja atualizar? (digite NOME SOBRENOME): ').strip().upper()
            if nome in lista_pacientes:
                posicao = lista_pacientes.index(nome)
                novo_nome = input('novo nome: ').strip().upper()
                novo_sobrenome = input('novo sobrenome: ').strip().upper()
                
                if novo_nome == '' or novo_sobrenome == '':
                    print('o nome e sobrenome nao podem ser em branco.')
                else:
                    lista_pacientes[posicao] = novo_nome + ' ' + novo_sobrenome
                    print('paciente alterado com sucesso!')
            else:
                print('paciente nao encontrado.')

        case 4:
            print('\n== REMOVER PACIENTE ==')
            nome = input('qual paciente deseja remover? (digite NOME SOBRENOME): ').strip().upper()
            if nome in lista_pacientes:
                lista_pacientes.remove(nome)
                print('paciente excluido com sucesso!')
            else:
                print('paciente nao encontrado.')

        case 5:
            print('\n== ENCONTRAR PACIENTE ==')
            nome = input('qual paciente deseja buscar? (digite NOME SOBRENOME): ').strip().upper()
            if nome in lista_pacientes:
                print('paciente encontrado com sucesso!')
            else:
                print('este paciente nao esta cadastrado.')

        case 0:
            print('saindo do programa...')
            break

        case _:
            print('opcao invalida! \nTente novamente...')

    input('pressione uma tecla para continuar...')