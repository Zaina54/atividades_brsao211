def calcular_desconto(preco, porcentagem):
    return preco * (porcentagem / 100)


preco = float(input("Digite o preço do produto: ").replace(",", "."))
desconto = float(input("Digite o desconto (%): ").replace(",", "."))

valor_desconto = calcular_desconto(preco, desconto)

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco - valor_desconto:.2f}")
