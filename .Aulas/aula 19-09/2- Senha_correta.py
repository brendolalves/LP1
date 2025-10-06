print("Senha")

password = input("Digite a senha: ")

correta = "123mudar"

while password != correta:
    print('senha errada, digite novamente: ')
    password = input("Digite a senha: ")
    if password == correta:
        print('Acesso permitido')