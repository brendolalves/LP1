#Exiba a tabuada de um número informado pelo usuário usando for
num = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Exiba a tabuada de um número informado pelo usuário usando while
num = int(input("Digite um número para ver sua tabuada: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1