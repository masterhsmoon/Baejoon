a = int(input())
c = 0
for i in range (1,a+1):
    x, y = map(int, input().split())
    z = x + y
    c = c+1
    print("Case #"+'{}: {} + {} = {}'.format(c,x,y,z))