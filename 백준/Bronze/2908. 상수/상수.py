a, b= map(str, input().split())

c = ''.join(reversed(a))
d = ''.join(reversed(b))
c = int(c)
d = int(d)

if c>d:
    print(c)
else:
    print(d)