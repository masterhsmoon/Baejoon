a = int(input())
if a>=1 and a<=100:
    for b in range (1,a+1):
        print(' '*(a-b)+'*'*b)