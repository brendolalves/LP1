"""
Exercício 3: Soma de Números *
 O usuário digita números para somar.
 O programa só para quando o usuário digita 0.
 No final, exibe a soma total dos números digitados.
"""
x=0


while x>=0:
    n= int(input("Digite um número (0 para sair): "))
    x = x + n
    if n==0:
       print("A soma dos números digitados é: ", x)
       break
    
    
    
