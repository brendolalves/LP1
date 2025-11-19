#Solicite um numero e inverta os digitos
n = int(input("Digite um número: "))
lista = [] 



for i in range(len(str(n))):
    x = n % 10**(i+1)
    lista.append(x // 10**i)        

print(lista)
numero = 0
for i in range(len(lista)):
    x_i = lista[i]*10**(len(lista)-i-1)
    print(x_i)
    numero += x_i
print(f'O número invertido é: {numero}')
    
# numero = lista[0]*10**(len(lista)) + lista[1]*10**(len(lista)-1) + lista[2]*10**(len(lista)-2) + lista[3]*10**(len(lista)-3)

#(f'O número invertido é: {numero}')