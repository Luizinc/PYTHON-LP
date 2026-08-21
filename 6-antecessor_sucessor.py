import os

# Limpo Terminal
os.system("cls")

print("= SOLICITANDO DADOS")
valor = int(input("digite o valor: "))

antecessor= valor -1
sucessor= valor +1

print ("n\ exibindo numero de dados")
print("o numero antecessor de", valor, "e" , antecessor)
print("o numero sucessor de", valor, "e" , sucessor)

