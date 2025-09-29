print("Senha correta")
print(" ")

senha = "123mudar"
digite = input('Digite a senha')

x=0
while x>0:
    print("Senha incorreta")
    digite = input('Digite a senha')
    x=x+1
    if digite == senha:
        print("Acesso permitido")
        break 
