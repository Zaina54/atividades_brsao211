import json

dados = {
    "nome": "João",
    "idade": 28,
    "cidade": "Belo Horizonte"
}

try:
    nome_arquivo = "dados.json"

    # Salvar JSON
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    # Ler JSON
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("Dados lidos do arquivo:")
    print(dados_lidos)

except Exception as e:
    print("Erro ao salvar ou ler o arquivo JSON:", e)
