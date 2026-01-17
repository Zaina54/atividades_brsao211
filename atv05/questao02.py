def eh_palindromo(texto):
    texto_limpo = ""

    for c in texto.lower():
        if c.isalnum(): 
            texto_limpo += c

    return texto_limpo == texto_limpo[::-1]

entrada = input("Digite uma palavra ou frase: ")

if eh_palindromo(entrada):
    print("Sim")
else:
    print("Não")
