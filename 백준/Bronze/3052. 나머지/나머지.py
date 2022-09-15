b = []


for i in range (0,10):
    a = int(input())
    c = a%42
    b.append(c)


b_set = set(b)
b = list(b_set)
print(len(b))