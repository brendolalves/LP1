#Solicite um número n e calcule o fatorial dele
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
if n < 0:
    print("Fatorial não definido para números negativos.")
elif n == 0 or n == 1:
    print("O fatorial de", n, "é 1.")
else: 
    for i in range(2, n + 1):
        fatorial *= i
    print("O fatorial de", n, "é", fatorial)