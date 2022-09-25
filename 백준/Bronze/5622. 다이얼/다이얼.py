a = list(input())
b = ['A','B','C']
c = ['D','E','F']
d = ['G','H','I']
e = ['J','K','L']
f = ['M','N','O']
g = ['P','Q','R','S']
h = ['T','U','V']
i = ['W','X','Y',"Z"]
sum = 0

for i in range(0,len(a)):
    if a[i] in b:
        sum = sum + 3
    elif a[i] in c:
        sum = sum + 4
    elif a[i] in d:
        sum = sum + 5
    elif a[i] in e:
        sum = sum + 6
    elif a[i] in f:
        sum = sum + 7
    elif a[i] in g:
        sum = sum + 8
    elif a[i] in h:
        sum = sum + 9
    else:
        sum = sum + 10
print(sum)   