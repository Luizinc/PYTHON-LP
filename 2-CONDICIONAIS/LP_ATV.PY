import os
os.system('cls')

#solicitando dados
usuario = (input('digite usuario: '))
senha = (input('digite sua senha: '))

#processamento
if usuario == 'luiz' and senha == '1234':
    print('acesso liberado')
else:
    print('usuario ou senha incorretas')


