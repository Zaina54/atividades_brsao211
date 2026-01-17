n1 = float(input("Digite o primeiro número: ").replace(",", "."))
n2 = float(input("Digite o segundo número: ").replace(",", "."))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        print("Erro: divisão por zero")
        exit()
else:
    print("Operação inválida")
    exit()

print(f"Resultado: {resultado:.2f}")
