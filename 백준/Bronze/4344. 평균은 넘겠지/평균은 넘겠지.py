a = int(input())
count = 0

for i in range (0,a):
    count = 0
    c = list(map(int, input().split()))
    b = c[0]
    c = c[1:b+1]
    d = sum(c)
    e = sum(c)/b
    for x in range (0,b):
        if c[x]>e:
            count = count +1
    g = count / b * 100
    print('%.3f' %g + '%')