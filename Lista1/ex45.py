n = int(input("Digite um número: "))
l = []

for i in range(1, n):
    if n % i == 0:
        l.append(i)
print(l)

soma = sum(l)
print("A soma dos divisores de", n, "é:", soma)

if soma == n:
    print(n, "é um número perfeito.")