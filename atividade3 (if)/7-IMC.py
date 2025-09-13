peso= float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

imc= peso/(alt*alt)

print("Seu IMC é: ", imc)

if imc <18.5:
    print('Abaixo do peso')
elif imc <24.9:
    print('Peso normal')
elif imc <29.9:
    print('Sobrepeso')
elif imc >30:
    print('Obesidade')