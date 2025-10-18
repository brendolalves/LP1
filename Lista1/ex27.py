#Solicite um número e exiba todos os seus divisores
num = int(input("Digite um número inteiro positivo: "))
print("Divisores de", num, "são:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
