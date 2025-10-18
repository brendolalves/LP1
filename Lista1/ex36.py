#Solicite um numero n e exiba os n primeiros numeros pares
l = []
n = int(input("Digite um número: "))
for i in range(n):
    if i % 2 == 0:
        l.append(i)
print("Os pares entre 0 e", n, "são:", l)
print("Quantidade de números pares:", len(l))