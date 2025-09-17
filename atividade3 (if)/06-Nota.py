nota = float(input("Digite a nota do aluno: "))

if nota <0:
    print("Nota inválida, digite novamente: ")
    nota = float(input("Digite a nota do aluno: "))


if nota<5:
    print("Reprovado")
if nota <6.9 and nota>=5:
    print("Recuperação")
if nota>=7:
    print("Aprovado")
