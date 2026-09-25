import os
os.system('cls')


nota = 0

for i in range (3):
    nota += float(input('digite sua nota: ' ))
    media= nota/3
print(f'a media e {media}')

if media >=7:
    print('aprovado')

elif media <=4:
    print('recuperaçao')
else:
    print ('reprovado')