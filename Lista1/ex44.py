"""l1 = []
l2 = []
n = int(input("Digite um número: "))
m = int(input("Digite outro número: "))
for i in range(1, n):
    if n % i == 0:
        l1.append(i)
        print(i)
for i in range(1, m):
    if m % i == 0:
        l2.append(i)
        print(i)
print("Divisores de", n, ":", l1)
print("Divisores de", m, ":", l2)

l3 = l1 + l2
print("Divisores combinados:", l3)
"""
n = int(input("Digite um número: "))
m = int(input("Digite outro número: "))
l = []
"""""
if n < m:
    i = m - n
    l.append(i)
if m < n:
    i = n - m
    l.append(i)
x = l[0]

if 
while x != 0:
    x = x - i
    l.append(x)
print(l)
"""""
x = max(n, m)
i = abs(n - m)
l.append(i)
print(l)


print(l)