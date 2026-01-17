qtd = int(input("Quantos alunos? "))
soma = 0

for i in range(qtd):
    nota = float(input(f"Digite a nota do aluno {i+1}: ").replace(",", "."))
    soma += nota

media = soma / qtd

print(f"Média da turma: {media:.2f}")
