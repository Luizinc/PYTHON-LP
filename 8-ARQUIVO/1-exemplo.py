from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome: str
    idade: int
    altura: float
    
QUANTIDADE_CLIENTES = 2

lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    novo_cliente = Clientes(
        nome = input('digite seu nome: '),
        idade = int(input('digite sua idade: ')),
        altura = float(input('digite sua altura: '))
    )
    lista_clientes.append(novo_cliente)
    
    #salvando em um arquivo.
    arquivo = 'dados_clientes.cvs'
    with open(arquivo, 'a') as arquivo_clientes:
        for cliente in lista_clientes:
            arquivo_clientes.write(f'{cliente.nome}, {cliente.idade}, {cliente.altura}\n')

    print('Cliente salvo com sucesso! \n')