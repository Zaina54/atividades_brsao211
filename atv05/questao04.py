from datetime import date

ano = int(input("Ano de nascimento: "))
mes = int(input("Mês de nascimento: "))
dia = int(input("Dia de nascimento: "))

data_nascimento = date(ano, mes, dia)
data_atual = date.today()

dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")
