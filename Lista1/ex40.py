#Solicite números até que o usuário digite 0 e exiba a soma deles.
l = []
n = int(input("Digite um número (0 para sair): "))
while n != 0:
    l.append(n)
    n = int(input("Digite um número (0 para sair): "))
print("A soma dos números digitados é:", sum(l))