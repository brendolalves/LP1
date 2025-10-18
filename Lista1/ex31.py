#Solicite 5 números e exiba o maior deles

l = []
for i in range(5):
    n = int(input("Digite um número: "))
    l.append(n)
print("O maior número é:", max(l))