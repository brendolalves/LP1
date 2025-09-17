a= float(input("Digite um lado do triângulo: "))
b= float(input("Digite o outro lado do triangulo: "))
c= float(input("Digite o ultimo lado do triangulo: "))

if a==b and c==b:
    print("Você possui um Triângulo Equilátero")
elif a==b or b==c or a==c:
    print("Você possuiu um Triângulo Isósceles")
elif a<b+c and c<b+a and b<a+c:
    print("Você possuiu um Triângulo Escaleno")
else:
    print("Os lados informados não formam un triângulo")