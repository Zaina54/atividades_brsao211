i = int(input("Digite sua idade: "))

if i <= 12:
    categoria = "Criança"
elif i <= 17:
    categoria = "Adolescente"
elif i <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Classificação: {categoria}")