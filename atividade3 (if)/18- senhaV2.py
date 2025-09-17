print("seu login é: BABANA")
print(" sua senha é: banana123")

login = "BANANA"
senha = "banana123"

#print("senha é: ", senha)
#print("login é: ", login)

l= str(input("digita seu login: "))


print(l)

if login == l:
    print("login ok")
else:
     print("login errado digite novamente")
     l = str(input("ditiga seu login: "))
     if login == l:
          print("agora está certo")
     else:
          print("login errado, você tem mais uma tentativa")
          l = str(input("digita seu login, com cuidado: "))
          if login == l:
               print("acesso permitido")
          else:
               print("acesso bloqueado")

s= str(input("digita sua senha: "))
print(s)

if senha == s:
    print("senha correta e acesso permitido")
else:
     print("senha errada digite novamente")
     l = str(input("ditiga sua senha: "))
     if senha == s:
          print("senha correta e acesso permitido")
     else:
          print("senha errada, você tem mais uma tentativa")
          l = str(input("digita sua senha, com cuidado: "))
          if senha == s:
               print("acesso permitido")
          else:
               print("acesso bloqueado")