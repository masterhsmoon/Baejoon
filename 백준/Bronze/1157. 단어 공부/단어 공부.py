A = input()
B = A.upper()
C = list(B)
D = set(B)
E = list(D)
F = []
for i in range(0,len(E)):
     F.append(C.count(E[i]))


if F.count(max(F)) == 1:
     print(E[(F.index(max(F)))])
else:
     print("?")