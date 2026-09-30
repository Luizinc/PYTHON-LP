import os
os.system('cls')

nota_total = 0

for i in range(2):
    
    while True:
        nota = float(input(f'Digite a nota {i+1}: '))
        
        if nota < 0 or nota > 10:
            print('\nNota incorreta, digite novamente.')
        else:
            print(f'Nota {nota} aceita com sucesso!\n')
            break
            
    nota_total += nota


media = nota_total / 2
print(f'A média final é: {media}')
