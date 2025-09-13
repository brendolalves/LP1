print("eai suave?")
test=True #atribuindo a variavel um valor booleano-lógico
print(test)
print(type(test)) #imprimindo a classe da variavel

#atribuindo a variável letras valores
a=1
b=5
c=2
d=1

#testado a lógica com as variáveis
print(a==d)
print(b>a)
print(a<b)
print(a==d)
print(c<=b)
print(d!=a)
print("novo teste")
a==c #não exibe sem o print

#usando a negação na operação, comando 'not'
print("comando not")
print(not a==d)

#usando a comporação na operação, comando 'and'
print('comando and')
print((a==b) and (a==c))
print((a==1) and (a==d))

#usando o comando "or"
print('comando or')
print((a==b) or (a==c))
print((a==1) or (a==d))
print((a==1) or (a==c))

salario=100
idade=20

print("fazendo a brincadeira com o salário")
print((salario > 1000) and (idade > 18)) 
print( (salario!=2000) and (idade<=25))
print((salario !=2000) and not (idade<=25))