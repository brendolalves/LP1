#Exiba apenas os números pares entre 1 e 30
print("Números pares entre 1 e 30 (com for):")
for i in range(1, 31):
    if i % 2 == 0:
        print(i)
print("-----")
#Exiba apenas os números ímpares entre 1 e 30 usando while
print("Números ímpares entre 1 e 30 (com while):")
i = 1
while i <= 30:
    if i % 2 != 0:
        print(i)
    i += 1