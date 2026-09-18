import os
os.system ('cls')

#INICIO
nome= input('digite seu nome: ')
nota1 = float(input('digite nota1: '))
nota2 =float(input('digite nota2: '))

#PROCESSAMENTO
media = (nota1 + nota2) /2

if media>= 9:
    resultado=print(f'o aluno{nome}foi aprovado com nota A')
elif media >= 7.5 and media < 9 :
    resultado=print(f'o aluno{nome}foi aprovado com nota B')
elif media >= 6 and media < 7.5:
    resultado=print(f'o aluno{nome}foi aprovado com nota C')
elif media >= 4 and media < 6:
    resultado=print(f'o aluno{nome}foi reprovado com nota D')
else: 
    resultado=print(f'o aluno{nome}foi reprovado com nota E')
