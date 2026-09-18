num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ").strip()

match operador:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2 if num2 != 0 else "Divisão por zero não permitida"
    case _:
        resultado = "Operador inválido"

print(f"\nPrimeiro número: {num1}")
print(f"Segundo número: {num2}")
print(f"Operador escolhido: {operador}")
print(f"Resultado: {resultado}")