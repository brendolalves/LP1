print("Vamos verificar a classificação da temperatura")
temp=float(input("Digite a temperatura atual: "))
print(" ")
print("Sendo a temperatura: ",temp)
if temp<=15:
    print("Frio")
elif temp<25:
    print("Agradável")
elif temp >=25:
    print("Quente")