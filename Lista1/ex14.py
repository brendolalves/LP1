#Peça dois números e informe qual é o maior e qual é o menor.
num1 = float(input("Digite o primeiro número: "))  
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior número é:", num1)
    print("O menor número é:", num2)
else:
    print("O maior número é:", num2)
    print("O menor número é:", num1)