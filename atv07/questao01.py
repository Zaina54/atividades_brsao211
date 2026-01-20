import pandas as pd

try:
    arquivo = input("Digite o nome do arquivo CSV: ")
    df = pd.read_csv(arquivo)

    media = df["tempo_execucao"].mean()
    maximo = df["tempo_execucao"].max()

    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Maior tempo de execução: {maximo:.2f}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
