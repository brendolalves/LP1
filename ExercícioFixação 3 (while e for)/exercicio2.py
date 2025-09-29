"""
Exercício 2:  Múltiplos de 5 até 50:
 • Exiba todos os múltiplos de 5 de 5 a 50.
"""

print("Usando o while")

x=0

while x<=50:
    x=x+1
    if x%5==0:
        print(x)
      


print(" ")
print("Usando o for")

for x in range(50):
    if (x+5)%5==0:
        print(x+5)
        