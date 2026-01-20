try:
    arquivo = input("Digite o nome do arquivo para salvar: ")

    pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 25, "São Paulo"],
        ["Carlos", 30, "Rio de Janeiro"],
        ["Marina", 22, "Curitiba"]
    ]

    with open(arquivo, "w", encoding="utf-8") as arquivo:
        for pessoa in pessoas:
            arquivo.write(f"{pessoa[0]}\t{pessoa[1]}\t{pessoa[2]}\n")

    print("Arquivo salvo com sucesso!")

except Exception as e:
    print("Erro ao salvar o arquivo:", e)
