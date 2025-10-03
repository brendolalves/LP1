"""
Exercício 5:Cálculo do Fatorial
 Escreva um programa em Python que solicite ao usuário um número inteiro n e calcule o fatorial 
desse número de duas formas:
 Usando um laço for
 Usando um laço while
"""
n = int(input('Digite o número: '))

fat = 1
i = 2 

while i<=n:
    fat = fat*i
    i = i + 1

print("o valor de %d! é = " %n, fat)

fat1 = 1
i1 = 2

for fat1 in range(n):

    fat1 = fat1*i1

    print("fatorial em for: ", fat1)
   

