A = int(input())
B = 0

for x in range(A):
    B = input()
    D = int(len(B))-2
    for y in range(D):
        print(B[y+2]*int(B[0]),end= "")
    print()