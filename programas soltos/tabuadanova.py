'''
Vamos contruir uma tabuada, onde o usuário irá digitar
o número então exibe sua tabuada
'''

numero = input('digite numero: ')
print('tabuada do: ', numero)
numero=int(numero)

for x in range(1, 11):
    print(str(x) +' x ' + str(numero) + " = " + str(x * numero)) #para usar o + juntar na mesma linha as variáveis tem que está em texto, srt 