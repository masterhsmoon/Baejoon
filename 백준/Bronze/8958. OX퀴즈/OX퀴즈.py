a = int(input())

for i in range (0,a):
    b = input()
    c = 0
    d = 0
    
    for x in range(0,len(b)):
                
                if b[x] == "O":
                    c = c+1
                    d = d + c
                else:
                    c = 0
    print(d)      