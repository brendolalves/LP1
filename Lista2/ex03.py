#Leia preços de produtos até que o usuário digite 0
total = 0.0
while True:
    preco = float(input("Digite o preço do produto (ou 0 para sair): "))
    if preco == 0:
        break
    total += preco
print(f"Total a pagar: R$ {total:.2f}")
if total > 100:
    print("Você ganhou um desconto de 10%!")
    total *= 0.9
    print(f"Total com desconto: R$ {total:.2f}")