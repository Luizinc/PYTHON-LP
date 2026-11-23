from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome:str
    telefone:str
    email:str
    
lista_cliente = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('digite seu nome: '),
        telefone = int(input('digite seu telefone: ')),
        email = input('digite seu e-mail: ')
    )
    lista_cliente.append(dados_do_cliente)
os.system('cls')
for cliente in lista_cliente:
    print('== EXIBINDO DADOS ==')
    print(f'Nome {cliente.nome}')
    print(f'Telefone {cliente.telefone}')
    print(f'Email {cliente.email}')