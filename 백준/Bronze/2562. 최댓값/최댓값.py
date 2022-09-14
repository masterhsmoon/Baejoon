b = []


for i in range (0,9):
    a = int(input())
    b.append(a)

c = b.index(max(b))
print(max(b))
print(c+1)