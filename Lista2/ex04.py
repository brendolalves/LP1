print("Digite 10 numeros")
numeros = []
pares = []
for _ in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)

print("Números digitados:", numeros)
print("A quantidade de números pares é:", len(pares))
print("A soma dos números pares é:", sum(pares))
