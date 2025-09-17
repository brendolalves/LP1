sal=float(input('Informe o seu salário atualmente R$'))

if sal< 2000:
    sal=sal+(sal*0.2)
    print('Seu novo salário é: RS',sal)
elif sal<4999.99:
    sal=sal+(sal*0.1)
    print("Seu novo salário é de: R$",sal)
elif sal>=5000:
    sal=sal+(sal*0.05)
    print('Seu novo salário é de R$',sal)
