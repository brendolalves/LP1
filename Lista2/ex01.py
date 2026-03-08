notas = []

qtd = int(input("Digite a quantidade de notas: "))
for i in range(qtd):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
media = sum(notas) / qtd
print(f"A média das notas é: {media:.2f}")