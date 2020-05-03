A, B = map(str, input().split())

j = 0
while j < len(A):
    try:
        if B.index(A[j]) != None:
            xCross = j
            break
    except Exception as e:
        j += 1

yCross = B.index(A[xCross])

base = [['.' for j in range(len(A))] for i in range(len(B))]

for i in range(len(B)):
    for j in range(len(A)):
        if i == yCross:
            base[i][j] = A[j]
        if j == xCross:
            base[i][j] = B[i]

for i in range(len(base)):
    for j in range(len(base[0])):
        print(base[i][j], end='')
    print()
