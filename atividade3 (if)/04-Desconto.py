id = int(input('Para ter o desconto digite sua idade: '))

if id <12 or id>59:
    print("Você tem direito ao desconto de 50%, o valor será de R$15,00")
else:
    print("você não tem direito ao desconto. O valor é de R$30,00")