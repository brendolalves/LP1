#Solicite uma senha numérica e repita a solicitação até o usuário digitar corretamente.
senha_correta = "1234"  # Defina a senha correta aqui
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")

print("Senha correta!")