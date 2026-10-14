import os
os.system('cls')

print('= inseririndo livros no vetor =')
vetor_livros = []

for i in range(5):
    livro = input('digite o nome do {i+1} livro: ')
    vetor_livros.append(livro)


print('\n= exibindo livros =')
for indice, livro in enumerate(vetor_livros, start=1):
    print(f'{indice}º: {livro}')



