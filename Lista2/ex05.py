n = int(input("Digite um número inteiro positivo: "))

p = 0
print("for")
for i in range(n):
    p = p + i
    print(p)
    if p > n:
        break



