import os
os.system('cls')



print("--- TESTE DO IF / ELIF / ELSE ---")
idade = int(input("Digite a sua idade para ver a categoria do ingresso: "))

# 1ª Regra: Se for menor de 12, entra aqui e ignora todas as linhas de baixo.
if idade < 12:
    print("Categoria: [INFANTIL] - Ganha um brinde de desenho animado!")

# 2ª Regra: Só olha aqui se a de cima for FALSA (ou seja, tem 12 anos ou mais).
elif idade < 18:
    print("Categoria: [ADOLESCENTE] - Tem direito a meia-entrada estudantil!")

# 3ª Regra: Só olha aqui se todas as anteriores forem FALSAS (tem 18 anos ou mais).
elif idade < 60:
    print("Categoria: [ADULTO] - Paga o valor inteito do ingresso.")

# Rede de segurança: Se não entrou em NENHUMA das regras de cima (idade maior ou igual a 60).
else:
    print("Categoria: [SÊNIOR] - Tem direito à gratuidade ou assento VIP!")

print("Fim da verificação. O Python executou apenas UM dos blocos acima.")
