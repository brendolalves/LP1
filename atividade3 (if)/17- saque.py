print("Vamos determinar a quantidade de notas no seu saque")
saque = int(input("Digite o valor do seu saque: R$"))

if saque%10 !=0:
    print('Valor inválido, o valor deve terminar em 0, carregue novamente o programa')
else: ("O valor desejado é R$",saque)

a = saque//100
saque1= saque -(a*100)

b= saque1//50
saque2= saque1 -(b*50)

c= saque2//20
saque3= saque2- (c*20)

d=saque3//10

print(a, "notas de 100")
print(b, 'notas de 50')
print(c, 'notas de 20')
print(d, 'notas de 10')