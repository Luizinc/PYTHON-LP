from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome:str
    telefone:str
    email:str
    
    
    def mostrar_dados(self):
        print(f'nome:{self.nome}')
        print(f'Telefone:{self.telefone}')
        print(f'Email:{self.email}')
        print('='*20)
    #funçao somente para envir e-mails
    def email_marketing(self):
        print(f'nome:{self.nome}')
        print(f'Email:{self.email}')
        print('='*20)
    
    def wattsapp_marketing(self):
        print(f'Nome:{self.nome}')
        print(f'Telefone:{self.telefone}')
        print('='*20)
    
lista_cliente = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('digite seu nome: '),
        telefone = int(input('digite seu telefone: ')),
        email = input('digite seu e-mail: ')
    )
    lista_cliente.append(dados_do_cliente)

os.system('cls')

print('\n= EXIBINDO DADOS =')
for cliente in lista_cliente:
    cliente.mostrar_dados()

print('\n= EXIBINDO E-MAIL MARKETING =')
for cliente in lista_cliente:
    cliente.email_marketing()
    
print('\n= EXIBINDO WATTSAPP MARKETING =')
for cliente in lista_cliente:
    cliente.wattsapp_marketing()