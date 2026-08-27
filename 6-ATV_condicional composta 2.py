import os

#LIMPA O TERMINAL
os.system("cls")

print("= SOLICITANDO DADOS =")
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
primeira_nota = float(input("digite a primeira nota: "))
segunda_nota = float(input("digite a segunda nota: "))
terceira_nota = float(input("digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print('APROVADO')
else :
    print('REPROVADO')

print("\n= EXIBINDO DADOS =")
print("Nome: ", nome)
print("idade: ", idade)
print("primeira nota: ", primeira_nota )
print("segunda nota: ", segunda_nota)
print("terceira nota: ", terceira_nota)
print("Media:", media)
