a, b = map(int, input().split())
c = int(input())

d = b + c
e = int(d/60)
f = d%60
g = a+e

if g >= 24:
      g = g-24

print(g,f)