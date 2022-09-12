a = int(input())
b = int(input())
z = 0
for i in range (1,b+1):
    x, y = map(int, input().split())
    z = x * y + z
    
if z==a:
    print("Yes")
else:
    print("No")