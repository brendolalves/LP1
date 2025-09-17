print("Vamos determinar se você tem direito ou não ao desconto na passagem")
S = "S"
N = "N"

estudante = input("Você é estuante? (S/N)")

#estudante = bool(estudante) ====== use o exemplo da senha, para a pessoa ter o desconto ela DEVE DIGITAR O S e para nao ter o desconto digita N

if estudante == S and estudante != N:
    print("Metade do preço")
elif estudante == N and estudante != S:
    print("Não tem direito ao desconto")
elif estudante != S and estudante != N:
    print('Resposta inválida, execute novamente o programa')
else: print('Vamos verificar sua idade')
id = int(input("Qual é a sua idade? "))

if id<6 or id>65 or estudante == S:
    print("Tarifa grátis se for criança ou idoso e desconto se for estudante")
else: print("Tarifa normal")
