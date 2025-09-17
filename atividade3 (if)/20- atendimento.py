print('Simulador de fila de atendimento')
print(' ')
esp=input('Você possui alguma dificiencia? (S/N)')
print(' ')
id=int(input('Qual é a sua idade?'))
print(' ')
gest=input('Você é gestante? (S/N)')
resp1="S"
resp2="N"
print(' ')

if gest==resp1:
        print('Você é gestante e possui prioridade média')
if esp==resp1 or id>=60:
    print("Você possui alguma dificiência ou é idoso então tem prioridade alta")
elif esp==resp2:
    print("Nessa categoria você não tem prioridade alta")
#else: 
    
else:("Você terá um atendimento normal")