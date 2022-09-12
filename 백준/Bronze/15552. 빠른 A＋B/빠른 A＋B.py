import sys

a = int(input())
for i in range (1,a+1):
    x, y = map(int, sys.stdin.readline().split())
    z = x + y
    print(z)