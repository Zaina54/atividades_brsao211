def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

conta = 150.00
porcentagem = 20

gorjeta = calcular_gorjeta(conta, porcentagem)
print(f"Gorjeta: R$ {gorjeta:.2f}")
