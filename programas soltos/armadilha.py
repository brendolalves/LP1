print("digitar algo até acontecer algo, esse algo é o break (parar)")

s = 0
while True:
    v = int(input("digite um valor diferente de zero")) 
    if v == 0:
        break #o que acontece, só consigo sair quando eu digitar
    s = s + v
print(s)