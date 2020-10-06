import sys


def getelement(mat1, mat2, column, row):
    element = 0
    for i in range(len(mat1[0])):
        element += (mat1[column][i] * mat2[i][row])
    return element


N, M = map(int, sys.stdin.readline().split())
matrix1 = []
for i in range(N):
    matrix1.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())
matrix2 = []
for i in range(M):
    matrix2.append(list(map(int, sys.stdin.readline().split())))

ans = [[0 for i in range(K)] for j in range(N)]
for i in range(N):
    for j in range(K):
        ans[i][j] = getelement(matrix1, matrix2, i, j)

for i in range(N):
    for j in range(K):
        print(ans[i][j], end=' ')
    print()
