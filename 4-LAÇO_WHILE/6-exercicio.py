import os
os.system('cls')


# Credenciais corretas cadastradas no sistema
LOGIN_CORRETO = "admin"
SENHA_CORRETA = "1234"

print("=== SISTEMA DE LOGIN ===")

# Laço infinito que só para quando tudo estiver correto
while True:
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    
    # O 'and' garante que o acesso só é liberado se AS DUAS condições forem verdadeiras
    if usuario == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\n[SUCESSO] Login efetuado com sucesso! Bem-vindo.")
        break  # Quebra o laço while e encerra o programa
    else:
        print("\n[ERRO] Login ou senha incorretos. Tente novamente.\n")
        print("-" * 30)
        input('precione uma tecla para continuar...')
        os.system('cls')
