#Solicite três notas e informe se a media é sufuciente para aprovação (média >= 6).
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print("Média suficiente para aprovação.")
else:
    print("Média insuficiente para aprovação.")
