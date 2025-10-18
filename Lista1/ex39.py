#Solicite um número n e exiba a tabuada de todos os números de 1 até n.
l = []
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    for j in range(1, 11):
        l.append(f"{i} x {j} = {i * j}")    
for linha in l:
    print(linha)
print("Tabuada de 1 até", n, "exibida acima.")

# --- IGNORE ---    
