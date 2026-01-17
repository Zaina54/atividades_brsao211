produto = "Camiseta"
preco = 50.00
desconto = 20
valor_desconto = preco * (desconto / 100)

print(f'''
    Produto: {produto}
    Preço original: R$ {preco:.2f}
    Desconto: {desconto}%
    Valor do desconto: R$ {valor_desconto:.2f}
    Preço final: R$ {preco - valor_desconto:.2f}
''')