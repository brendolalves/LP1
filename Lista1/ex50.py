#Simule um caixa eletrônico (como no exercício que você mostrou, decompondo notas).
def decompor_valor(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    contagem_notas = {}
    
    for nota in notas:
        if valor >= nota:
            quantidade = valor // nota
            contagem_notas[nota] = quantidade
            valor -= quantidade * nota
            
    return contagem_notas
def caixa_eletronico():
    valor = int(input("Digite o valor a ser sacado: R$ "))
    contagem_notas = decompor_valor(valor)
    
    print("Você receberá:")
    for nota, quantidade in contagem_notas.items():
        print(f"{quantidade} nota(s) de R$ {nota}")
caixa_eletronico()
