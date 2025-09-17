print("seu login é: BABANA")
print(" sua senha é: banana123")

login = "BANANA"
senha = "banana123"

print("senha é: ", senha)
print("login é: ", login)

l= str(input("digita seu login: "))
s= str(input("digita sua senha: "))

print(l)
print(s)

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
               print("ufa está certo")
          else:
               print("acesso bloqueado")