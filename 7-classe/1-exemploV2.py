from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #variavel: tipo da variavel
    nome: str
    idade: int

#solicitando dados de um cliente
cliente1 = Cliente('Marta', 30)

#solicitando dados de outro cliente
cliente2 = Cliente('José', 40)

print(f'Nome: {cliente1.nome}')
print(f'Idade: {cliente1.idade}')

print(f'Nome: {cliente2.nome}')
print(f'Idade: {cliente2.idade}')
