import os

# Limpo Terminal
os.system("cls") 

#ENTRADA.
print('SOLICITANDO DADOS =')
primeiro_numero = float(input('digite o primeiro numero: '))
segundo_numero = float(input('digite o segundo numero: '))


#PROCESSAMENTO.
soma =primeiro_numero + segundo_numero
subtracao=primeiro_numero - segundo_numero
multiplicacao=primeiro_numero * segundo_numero
divisao=primeiro_numero / segundo_numero

#SAIDA.
print('\n= EXIBINDO DADOS =')
print('soma: , soma')
print('subtracao: , subtracao')
print('multiplicacao: , multiplicacao')
print('divisao: , divisao')