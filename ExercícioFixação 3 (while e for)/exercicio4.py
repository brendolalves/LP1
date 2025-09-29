"""
Exercício 4: Caixa Eletrônico:
 • O usuário informa um valor e o programa calcula 
as notas necessárias (100, 50, 20, 10, 5, 
2, 1).
"""

cash = int(input("Qual o valor da retirada?: "))
x= 0
peixe = 0

while x <=cash:
    x = x*100 + peixe
    print(x)

    