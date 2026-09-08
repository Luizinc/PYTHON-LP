import os
os.system('cls')

ano_de_nascimento = int(input("Digite o ano de nascimento: "))
sexo = input("Digite o sexo (M/F): ")

if sexo.upper() == "M":
    idade = 2026 - ano_de_nascimento
    print("Idade: ", idade)
    if idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você é maior de idade, precisa se se alistar!.")
elif sexo.upper() == "F":
    idade = 2026 - ano_de_nascimento
    print("Idade: ", idade)
    if idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você é maior de idade.")

    else:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")