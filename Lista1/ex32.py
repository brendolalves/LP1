# Solicite 5 números e exiba o menor deles
l = []
for i in range(5):
    n = int(input("Digite um número: "))
    l.append(n)
print("O menor número é:", min(l))