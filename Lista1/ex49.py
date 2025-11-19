#Simule uma calculadora simples (soma, subtração, multiplicação, divisão).
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."    
def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite a opção (1/2/3/4): ")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        print(f"{num1} + {num2} = {soma(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Opção inválida.")
calculadora()
