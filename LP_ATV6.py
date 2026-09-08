import os
os.system('cls')

# Solicitando as informações ao usuário
matricula = input("Digite a matrícula do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
tempo_trabalho = int(input("Digite o tempo de trabalho (em anos): "))

# Calculando a idade do empregado com base no ano atual
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

# Verificação da condição de aposentadoria (mínimo 65 anos de idade OU 30 anos de trabalho)
if idade >= 65 or tempo_trabalho >= 30:
    mensagem = "Requerer aposentadoria"
else:
    mensagem = "Não requerer aposentadoria"

# Exibição dos resultados
print("\n--- Resultado ---")
print(f"Código do empregado: {matricula}")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_trabalho} anos")
print(f"Situação: {mensagem}")