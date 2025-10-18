#Peça uma nota de 0 a 10 e informe se o aluno foi aprovado (nota >= 7), reprovado (nota < 5) ou em recuperação (5 <= nota < 7).
nota = float(input("Digite a nota do aluno (0 a 10): "))
if nota >= 7:
    print("Aluno aprovado.")
elif nota < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em recuperação.")