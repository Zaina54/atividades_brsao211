try:
    arquivo = input("Digite o nome do arquivo para leitura: ")

    with open(arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
