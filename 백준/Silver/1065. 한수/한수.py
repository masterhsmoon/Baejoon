N = int(input())
count = 0
for i in range(0,N):
    R = N-i
    a = R//100 
    b = R//10 - a*10
    c = R - a*100 - b*10
    
    if R<100: 
        count = count +1
    elif 100 <= R < 1000: 
        if a-b == b-c:
            count = count +1

print(count)