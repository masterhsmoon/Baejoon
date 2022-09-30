a = int(input())
x = 1
while True:
    if a-6*x > 1:
        a = a-6*x
        x += 1
    elif a == 1:
        print(x)
        break
    else:
        print(x+1)
        break