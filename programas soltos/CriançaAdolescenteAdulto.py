id=input("digite sua idade")
print("sua idade é: ", id)

id=int(id)

if id < 12:
    print("Criança")
elif id < 18:
    print("Adolescente")
else:
    print("Adulto")