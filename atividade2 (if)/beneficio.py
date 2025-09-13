idade = int(input("qual é a sua idade? "))
salario = int( input("qual é o seu salário? "))
print("sua idade é: ", idade)
print( "Seu salário é:", salario)

if idade > 18 and salario <= 2000:
    print("Tem direito ao benefício ")
else: 
    print( "Não tem direito ao benefício ")