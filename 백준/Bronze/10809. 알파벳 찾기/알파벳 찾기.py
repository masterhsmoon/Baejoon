A = list(input())

for i in range(26):
    if chr(i+97) in A:
        B = A.index(chr(i+97))
        print(B, end=' ')
    else:
        print(-1, end=' ')