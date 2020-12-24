import sys


def main():
    global N, minPrice, price
    N = int(sys.stdin.readline())
    minPrice = 3001
    price = []
    board = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        price.append(list(map(int, sys.stdin.readline().split())))
    seed = []
    dfs(seed, board, 0)
    print(minPrice)


def dfs(seed, board, cnt):
    global N, minPrice, price
    dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    dy2, dx2 = [-2, 2, 0, 0], [0, 0, -2, 2]
    if cnt != 3:
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                flag = 1
                for k in range(9):
                    if board[i + dy[k]][j + dx[k]] == 1:
                        flag = 0
                        break
                for k in range(4):
                    if 0 <= i + dy2[k] < N and 0 <= j + dx2[k] < N:
                        if board[i + dy2[k]][j + dx2[k]] == 1:
                            flag = 0
                            break
                if flag:
                    seed.append([i, j])
                    board[i][j] = 1
                    dfs(seed, board, cnt + 1)
                    seed.pop()
                    board[i][j] = 0
    else:
        pdy, pdx = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0] #price를 구할떄 씀
        tmpPrice = 0
        for point in seed:
            y, x = point[0], point[1]
            for i in range(5):
                tmpPrice += price[y + pdy[i]][x + pdx[i]]
        if tmpPrice <= minPrice:
            minPrice = tmpPrice


if __name__ == '__main__':
    main()
