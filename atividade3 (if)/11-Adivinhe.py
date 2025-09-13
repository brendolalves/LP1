print("Adivinhe o número secreto entre 0 a 100")
num=7
print("  ")
n=int(input('Digite o número: '))
if n==num:
    print("Parabéns")
elif n<num:
    print('Muito baixo')
elif n>num:
    print('Muito alto')