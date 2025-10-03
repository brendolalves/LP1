"""
tupla é uma lista constante, que usa os parenteres 
não conseguimos adicionar, apagar editar no qual ela se altera, isto é ela 
se torna uma nova tupla
"""

professores_fatec = [('Orlando', 'LP1'), ('Henri', 'Iot')]


tupla2 = 100, 200, 300

a, b = 10, 20

a,b,c = tupla2

print(tupla2)


lista = list(tupla2)
a, b, c, = lista
tupla3 = tuple(lista)

a = set()
a.add(1)
a.add(2)
a.add(3)
a.add(-1)
a.add(1)

print(a)


"""
diconario: relaciona chave e seu valor. e pode ser mudavel
"""

tabela = {'Arroz 5kg': 24.99, 
          'Feijão 1kg': 1 } #continua


#se não tiver o elemento, podemos add do seguinte modo -- "Açúcar 5kg': 10

#hash mostra que cada chave tem identificacao unica

#get, podemos colocar uma mensagem que não encontrei (veja na documentação)