n = int(input("Digite um número: "))
list = []


for i in range(100):
   x = n % 10**i
   list.append(x)
   x = x - list[i]
print(list)