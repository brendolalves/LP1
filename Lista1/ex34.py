#solicite 10 números e conte quantos são pares
l = []
count = 0
for i in range(10):
    n = int(input("Digite um número: "))
    if n % 2 == 0: #cada entrada de um par é marcada e somada com 1
     count += 1
     l.append(count)
print("Quantidade de números pares:", len(l))