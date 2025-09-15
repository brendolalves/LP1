print("Vamos determinar se você tem direito ou não ao desconto na passagem")
S = True
N = False
id = int(input("Qual é a sua idade? "))
estudante = input("Você é estuante? (S/N)")

#estudante = bool(estudante) ====== use o exemplo da senha, para a pessoa ter o desconto ela DEVE DIGITAR O S e para nao ter o desconto digita N

if estudante == S and estudante != N:
    print("Metade do preço")
elif id<6 or id>65:
    print("Tarifa grátis")
else: print("Tarifa normal")

