a = list(range(1,10000))

for i in range(1,10000):
    b = i // 10000
    c = i // 1000 - b*10
    d = i // 100 - b*100 - c*10
    e = i // 10 - b*1000 - c*100 - d*10
    f = i - b*10000 - c*1000 - d*100 - e*10
    g = i
    
    h = c+d+e+f+g
  
    if h in a:
        a.remove(h)
    
for i in a:
    print(i)
     