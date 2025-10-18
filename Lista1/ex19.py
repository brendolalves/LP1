#Solicite um ano e verifique se é bissexto (divisível por 4, mas não por 100, exceto se for divisível por 400).
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
