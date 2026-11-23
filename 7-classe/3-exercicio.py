from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Paciente:
    nome:str
    idade:str
    telefone:str
    endereco: str
    
    
    def mostrar_dados(self):
        print(f'nome:{self.nome}')
        print(f'Idade:{self.idade}')
        print(f'Telefone:{self.telefone}')
        print(f'Endereço:{self.endereco}')
        print('='*20)
        
    def mostrar_nome_idade(self):
        print(f'nome:{self.nome}')
        print(f'idade:{self.idade}')

    def mostrar_nome_telefone(self):
        print(f'nome:{self.nome}')
        print(f'telefone:{self.telefone}')

lista_paciente = []

for i in range(1):
    dados_do_paciente = Paciente(
        nome = input('digite seu nome: '),
        idade = int(input('digite sua idade: ')),
        telefone = int(input('digite seu telefone: ')),
        endereco = input('digite seu endereço: ')
    )
    lista_paciente.append(dados_do_paciente)

os.system('cls')

print('\n= EXIBINDO DADOS =')
for paciente in lista_paciente:
    paciente.mostrar_dados()

print('\n= EXIBINDO NOME E IDADE =')
for paciente in lista_paciente:
    paciente.mostrar_nome_idade()

print('\n= EXIBINDO NOME E TELEFONE =')
for paciente in lista_paciente:
    paciente.mostrar_nome_telefone()