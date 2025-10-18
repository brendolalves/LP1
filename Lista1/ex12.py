#solicite um número interio ao usuário e informe se ele é positivo, negativo ou zero.
numero = int(input("Digite um número inteiro: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")