#a hastag é o comentário, e coloquei o que cada linha está fazendo 
# --------------------Programa da Senha--------------------


print("seu login é: BABANA") #nessa linha está determinada o seu login
print(" sua senha é: banana123") #nessa linha está determinada a sua senha

login = "BANANA" #variavel para comparação do login
senha = "banana123" #variavel para a comparação da senha

l= str(input("digita seu login: ")) #aqui é a variavel que recebe suas entradas de login
s= str(input("digita sua senha: ")) #aqui é a variavel que recebe suas entradas de senha
print("você digitou login como: ", l) #exibe seu login
print("você digitou a senha como: ", s) #exibe sua senha

if login == l and senha==s: #aqui compara o que você digitou como login e senha com o que foi atribuido no início
    print("login ok") #se vc digitou certo, então está exibindo que está liberado
else: #se digitou errado algo então entramos aqui
     print("login errado digite novamente") #frase que está pedindo pra digitar novamente
     l = str(input("ditiga seu login: ")) #o que digitar será seu login
     s = str(input("ditiga sua senha: ")) #o que digitar será sua senha

     if login == l and senha==s: #compara novamente com o que digitou com o que foi determindo
          print("agora está certo") #se está batendo está ok
     else: #entra novamente no ciclo
          print("login errado, você tem mais uma tentativa")
          l = str(input("digita seu login, com cuidado: "))
          s = str(input("ditiga sua senha: "))
          if login == l and senha==s:
               print("acesso permitido")
          else: #após três tentativas, o aceeso é bloqueado, BASTA NÃO PEDIR MAS NADA AO USUÁRIO    
               print("acesso bloqueado") #exibe que o seu acesso está bloqueado

