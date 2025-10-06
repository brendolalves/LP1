l1=[1,2,3,4,5]

l2=[3,4,5,6,7]

l3 = l1

for elemento in l2:
    if elemento in l3:
        print('Não add elemento' + str(elemento))
    else:
        l3.append(elemento)
        print(l3)

        

