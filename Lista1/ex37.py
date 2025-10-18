# Solicite um numero n e exiba apenas a soma dos n primeiros numeros impares
l = []
n = int(input("Digite um número: "))
for i in range(n):
    if i % 2 != 0:
        l.append(i)
print("Os ímpares entre 0 e", n, "são:", l)
print("A soma dos ímpares entre 0 e", n, "é:", sum(l))