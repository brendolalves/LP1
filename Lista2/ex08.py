n = int(input("Digite um número inteiro positivo: "))

i = 1

for i in range(n):
    for j in range(i+1):
        print(i , end=" ")
    print()
