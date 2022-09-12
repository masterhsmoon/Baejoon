a, b = map(int, input().split())
d = b + 15
if d>=60:
    d = d - 60
           
    print(a,d)
else:
    c = a - 1
    if c<0:
        c = 23
    print(c,d)