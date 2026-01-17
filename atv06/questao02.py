import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()["results"][0]

    nome = f"{dados['name']['first']} {dados['name']['last']}"
    email = dados['email']
    pais = dados['location']['country']

    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except requests.RequestException:
    print("Erro ao acessar a API de usuário.")
