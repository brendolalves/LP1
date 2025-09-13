print('Vamos transformar a nota numérica para conceito')
nota=float(input("Digite a nota: "))

if 9<=nota<=10:
    print("Nota A")
elif nota>7:
    print('Nota B')
elif nota>5:
    print('Nota C')
elif nota >3:
    print("Nota D")
elif nota>0:
    print('Nota E')
else:
    ("Nota inválida")