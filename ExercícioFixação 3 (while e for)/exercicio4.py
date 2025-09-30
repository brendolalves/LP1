"""
Exercício 4: Caixa Eletrônico:
 • O usuário informa um valor e o programa calcula 
as notas necessárias (100, 50, 20, 10, 5, 
2, 1).
"""

cash = int(input("Qual o valor da retirada?: "))
cem = 0

while cem*100 <=cash:
    print(cem, " notas de 100")
    cem=cem+1
r1= cash-((cem-1)*100)
print(r1)
ciq=0
while ciq*50<=r1:
    print(ciq, " notas de 50")
    ciq=ciq+1
r2 = r1-((ciq-1)*50)
print(r2)
vin=0
while vin*20<=r2:
    print(vin, " notas de 20")
    vin=vin+1
r3=r2-((vin-1)*20)
print(r3)
dez=0
while dez<=r3:
    print(dez, " notas de 10")
    dez=dez+1
