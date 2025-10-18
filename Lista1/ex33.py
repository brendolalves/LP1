#Solicite 5 numeros e calcule a média deles
l = []
for i in range(5):
    n = int(input("Digite um número: "))
    l.append(n)
media = sum(l) / len(l)
print( sum(l)/len(l))
print("A média dos números é:", media)