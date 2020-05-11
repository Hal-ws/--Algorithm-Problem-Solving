N = int(input())

center = 2 * (N - 1)
size = 4 * N - 3

plate = [[' ' for i in range(4 * N - 3)] for j in range(4 * N - 3)]

plate[center][center] = '*'

for i in range(N):
    start = center - 2 * i
    end = center + 2 * i
    for j in range(start, end + 1):
        plate[start][j] = '*'
        plate[j][start] = '*'
        plate[end][j] = '*'
        plate[j][end] = '*'

for i in range(size):
    for j in range(size):
        print(plate[i][j], end='')
    print()
