import os
os.system('cls')

LOGIN_CORRETO = "luiz"
SENHA_CORRETA = "1234"

print("=== SISTEMA DE LOGIN ===")


while True:
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    

    if usuario == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\n[SUCESSO] Login efetuado com sucesso! Bem-vindo.")
        break
    else:
        print
