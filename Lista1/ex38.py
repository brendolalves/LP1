# Solicite um numero n e exiba quantos numeros entre 1 e n são multipos de 7
n = int(input("Digite um número: "))
l = []
count = 0
for i in range(1, n + 1):
    if i % 7 == 0:
        count += 1
        l.append(i)
print("Os múltiplos de 7 entre 1 e", n, "são:", l)
print("Quantidade de múltiplos de 7 entre 1 e", n, "é:", count)