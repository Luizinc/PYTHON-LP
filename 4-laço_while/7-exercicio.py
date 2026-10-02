import os
os.system('cls')




LOGIN_CORRETO = input('cadastre seu nome de usuario: ').strip()
SENHA_CORRETA = input('coloque sua senha: ').strip()

print("=== SISTEMA DE LOGIN ===")


for i in range(3):
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    
    if usuario == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\n[SUCESSO] Login efetuado com sucesso! Bem-vindo.")
        break
    else:
        print("\n[ERRO] Login ou senha incorretos. Tente novamente.\n")
        print("-" * 30)
        input('precione uma tecla para continuar...')
        
        os.system('cls')
print('=== FIM ===')