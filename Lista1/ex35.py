#solicite 10 números e conte quantos são positivos
l = []
count = 0
for i in range(10):
    n = int(input("Digite um número: "))
    if n > 0: #cada entrada de um número positivo é marcada e somada com 1
        count += 1
        l.append(count)
print("Quantidade de números positivos:", len(l))