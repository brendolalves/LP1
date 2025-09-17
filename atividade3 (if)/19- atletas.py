print('Classificador de atletas')
id=int(input('Digite a idade do atleta: '))

if id <=12:
    print('Infantil')
elif id <=17:
    print('Juvenil')
elif id <=40:
    print('Adulto')
elif id>40:
    print('Veterano')