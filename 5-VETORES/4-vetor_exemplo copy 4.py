import os
os.system('cls')

print('= inseririndo livros no vetor =')
vetor_livros = []

for i in range(5):
    livro = input('digite o nome de um livro: ')
    vetor_livros.append(livro)


print('\n= exibindo livros =')
for index in range(5):
    print(f'nome: {vetor_livros[index]}')



