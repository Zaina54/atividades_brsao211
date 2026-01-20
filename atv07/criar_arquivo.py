import pandas as pd

dados = {
    "tempo_execucao": [1.5, 2.3, 0.9, 4.1, 3.0]
}

df = pd.DataFrame(dados)

df.to_csv("dados_teste.csv", index=False)

print("Arquivo 'dados_teste.csv' criado com sucesso!")
