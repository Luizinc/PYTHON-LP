from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #variavel: tipo da variavel
    nome: str
    idade: int

lista_clientes = []

#solicitando dados de um cliente
lista_clientes.append(Cliente(nome='Marta', idade=30))
lista_clientes.append(Cliente(nome='José', idade=40))

#solicitando dados de outro cliente
cliente2 = Cliente('José', 40)

for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'='*11)