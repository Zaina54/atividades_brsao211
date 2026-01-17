import requests

cep = input("Digite o CEP: ").replace("-", "").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")

except requests.RequestException:
    print("Erro ao consultar o CEP.")
