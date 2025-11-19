l = []
n = int(input("Digite um número"))

m = []

for i in range(n-2):
    l.append(i+2)
    if n % l[i] == 0:
        m.append(l[i])
if len(m) == 0:
        print("Número primo")

print(l)
print(m)
