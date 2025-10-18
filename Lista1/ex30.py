#Solicite um numero n e exiba a soma dos numeros de 1 a n
n = int(input("Digite um número inteiro positivo: "))  
if n < 1:
    print("Número inválido. Por favor, digite um número inteiro positivo.")
else:
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print("A soma dos números de 1 a", n, "é:", soma)