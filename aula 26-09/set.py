A= set(list(range(1,10)))
print("A =", A)
B= set(list(range(5,15)))
print("B = ", B)
C= set(list(range(9,20)))
print("C =", C)


print("A inter B inter C = ", A.intersection(B).intersection(C))

print(A-C)

print(A.difference(C).intersection(B))


