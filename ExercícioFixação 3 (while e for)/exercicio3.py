"""
Exercício 3: Soma de Números Pares:
 • Peça um número e some apenas os números pares de 1 até ele.
"""

print("Com o while")

x = int(input("Digite um número: "))
n=0
s=0
while n<x:
    n=n+1
    if n%2==0:
        s=n+s
print(s)

print(" ")
print("Usando o for")

m=0
t=0

for m in range(x):
    if (m+2)%2==0:
        t=(m+2)+t
print(t)
