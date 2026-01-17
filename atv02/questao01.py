reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

print(f'''
    Valores:
      Reais: R$ {reais:.2f}
      Dólares: U$ {reais / taxa_dolar:.2f}
      Euros: € {reais / taxa_euro:.2f}
''')