import sys


def multiple(mat1, mat2):
    result = [[0 for i in range(N)] for j in range (N)]
    for i in range(N):
        for j in range(N):
            element = 0
            for k in range(N):
                element += mat1[i][k] * mat2[k][j]
            result[i][j] = element % 1000
    return result

def dnc(mat, degree):
    if degree == 1:
        for i in range(N):
            for j in range(N):
                mat[i][j] = mat[i][j] % 1000
        return mat
    elif degree == 2:
        return multiple(mat, mat)
    elif degree % 2 == 0:
        temp = dnc(mat, degree // 2)
        return multiple(temp, temp)
    else:
        temp = dnc(mat, degree // 2)
        return multiple(multiple(temp, temp), matrix)

N, B = map(int, sys.stdin.readline().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

matrix = dnc(matrix, B)
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end =' ')
    print()
