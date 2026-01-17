pares = 0
impares = 0

while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")

    if entrada.lower() == "sair":
        break

    numero = int(entrada)

    if numero % 2 == 0:
        pares += 1
        print("Número par")
    else:
        impares += 1
        print("Número ímpar")

print(f"""
Total de números pares: {pares}
Total de números ímpares: {impares}
""")
