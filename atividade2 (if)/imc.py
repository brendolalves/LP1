peso = float(input ("Qual é seu peso? (em quilo.grama)"))
print('Seu peso é: ', peso)
alt = float(input("Qual é a sua altura? (em metro.centimetro)"))
print('Sua altura é:', alt)

imc = peso/(alt*alt)

print("O IMC é: ", imc)

if imc < 18.5:
    print("Abaixo do peso em kilo")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("sobrepeso")
elif imc < 34.9:
    print("obsidade grau 1")
elif imc < 39.9:
    print("obsesidade grau 2")
elif imc >40:
    print("obsidade grau 3")