#Solicite um numero n e exiba os n primeiros multiplos de 3
n = int(input("Digite um número inteiro positivo: "))
if n < 1:
    print("Número inválido. Por favor, digite um número inteiro positivo.")
else:
    print("Os primeiros", n, "múltiplos de 3 são:")
    for i in range(1, n + 1):
        print(3 * i)