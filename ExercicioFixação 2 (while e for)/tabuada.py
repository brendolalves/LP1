#Peça um número ao usuário e exiba a tabuada desse número de 1 a 10.

n = int(input('Digita um número: '))

for x in range(10):
    m = n*(x+1)
    print(n, "X", x+1 ,"= ", m)