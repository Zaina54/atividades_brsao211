p = int(input("Digite seu peso (kg): "))
a = float(input("Digite sua altura: ").replace(",", "."))

imc = p / (a ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f'''
    IMC: {imc:.2f}
    Classificação: {classificacao}
''')