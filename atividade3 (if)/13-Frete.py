print("Vamos calcular o frete")
frete=float(input("Digite o valor do produto: "))

if frete>100:
    print("Frete é grátis e o preço atual é R$",frete)
elif frete<=100:
    frete=frete+15
    print("o frete é R$15,00 e seu preço atual é R$",frete)
