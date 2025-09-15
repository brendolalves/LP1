print("Vamos calcular a aliquota do Imposto de Renda")
sal = float(input("Digite o seu salário R$"))

if sal<= 1900:
    print("Isento")
elif sal <= 2800:
    print("Aliquota de 7,5%")
    desc=(sal-1900)*0.075
    print('O valor da aliquota será: R$',desc)
elif sal<= 3700:
    print('Aliquota de 15%')
    desc=(sal-1900)*0.15
    print('O valor da aliquota será: R$',desc)
elif sal <= 4600:
    print('Aliquota de 22,5%')
    desc=(sal-1900)*0.225
    print('O valor da aliquota será R$',desc)
elif sal> 4600:
    print('Aliquota de 27,5%')
    desc=(sal-1900)*0,275
    print('O valor da aliquota é R$',desc)
