from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str

QUANTIDADE_FORNECEDOR = 1
lista_fornecedor = []

for i in range(QUANTIDADE_FORNECEDOR):
    novo_fornecedor = Fornecedor(
        nome = input('digite seu nome: '),
        email = input('digite seu e-mail: '),
        telefone = input('digite seu telefone: '),
        endereco = input('digite seu endereço: ')
    )
    lista_fornecedor.append(novo_fornecedor)
    
    #salvando em um arquivo.
    arquivo = 'dados_fornecedores.cvs'
    with open(arquivo, 'a') as arquivo_fornecedor:
        for fornecedor in lista_fornecedor:
            arquivo_fornecedor.write(f'{fornecedor.nome}, {fornecedor.email}, {fornecedor.telefone}, {fornecedor.endereco} \n')

    print('fornecedor salvo com sucesso! \n')
print('\nExibindo dados dos clientes:')

for fornecedor in lista_fornecedor:
    print(f'Nome: {fornecedor.nome}')
    print(f'E-mail: {fornecedor.email}')
    print(f'Telefone: {fornecedor.telefone}')
    print(f'Endereco: {fornecedor.endereco}')
    print('==========================')
