#Solicite um núemro n e exiba os n primeiros números naturais
n = float(input("Digite um número inteiro positivo: "))
if n < 0 or n != int(n):
    print("Número inválido. Por favor, digite um número inteiro positivo.")
else:
    n = int(n)
    print("Os primeiros", n, "números naturais são:")
    for i in range(n):
        print(i)