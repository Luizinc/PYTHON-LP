import os
os.system('cls')

media = 0



for i in range(3):
    
    while True:
        nota = float(input(f'Digite a nota {i+1}: '))
        
        if nota <0 :
            print('\n APROVADO.')
        else:
            print('\n REPROVADO.')
            break
            
    nota_total += nota


media = nota_total / 3
print(f'A média final é: {media}')
