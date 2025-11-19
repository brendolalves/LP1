#Solicite um número n e exiba a sequência de Fibonacci até o n-ésimo termo.

l = []
n = int(input("Digite um número: "))
m=1
#l[0]=1
for i in range(n):
    l.append(m)
    m =l[i]+l[i-1]
    print(i,m)
print(l)
print("O", n,"-ésimo termo da sequência de Fibonacci é:", l[n-1])