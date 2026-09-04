import random


# O computador escolhe um número aleatório de 1 a 5
numero_secreto = random.randint(1, 5)

print("--- JOGO DE ADIVINHAÇÃO ---")
# Solicita o palpite do usuário e converte para número inteiro (int)
palpite = int(input("Adivinhe o número que estou pensando (de 1 a 5): "))

# Validação com as funções lógicas (Verifica se está fora do intervalo)
if palpite < 1 or palpite > 5:
    print("Aviso: Seu palpite precisa ser entre 1 e 5!")
# Compara se o palpite é igual ao número secreto
elif palpite == numero_secreto:
    print(f"Parabéns! Você acertou. O número era {numero_secreto}.")
else:
    print(f"Que pena, você errou! O número correto era {numero_secreto}.")
