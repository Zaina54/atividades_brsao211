temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

# Converter para Celsius
if origem == "C":
    temp_c = temp
elif origem == "F":
    temp_c = (temp - 32) * 5/9
elif origem == "K":
    temp_c = temp - 273.15
else:
    print("Unidade de origem inválida")
    exit()

# Converter de Celsius para destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida")
    exit()

print(f"Temperatura convertida: {resultado:.2f} {destino}")
