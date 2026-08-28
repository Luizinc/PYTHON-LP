import os

# Limpo Terminal
os.system("cls")


#ENTRADA
idade = int(input('Digite sua idade: '))





#PROCESSAMENTO.
if idade < 16:
    print('nao pode votar')
elif idade < 18:
    print('voto opcional.')
elif idade < 65:
    print('voto obrigatorio.')
else: 
    print('nao e obrigado a votar.')


print("-" * 30)



# saida
print('FIM DO PROGRAMA')