import random
secreto = random.randint(1, 50)
#print("Número gerado:", secreto)

numero = int(input("Adivinhe o número entre 1 e 50: "))
while numero != secreto:
    if numero < secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    numero = int(input("Adivinhe o número entre 1 e 50: "))

print("Parabéns! Você adivinhou o número.")
