from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #variavel: tipo da variavel
    nome:str
    idade:int
    altura:float
    peso: float
    
lista_clientes = []

#solicitando dados de um cliente
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('\ndigite seu nome: '),
        idade = int(input('digite sua idade: ')),
        altura = float(input('digite sua altura: ')),
        peso = float(input('digite seu peso: '))
    )
    lista_clientes.append(dados_do_cliente)
os.system('cls')

print('\nEXIBINDO DADOS')
for cliente in lista_clientes:
    print(f'='*11)
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print(f'Peso: {cliente.peso}')
    print(f'='*11)