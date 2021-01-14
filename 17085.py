import sys
from itertools import product, permutations


def main():
    global N, M, board, points
    N, M = map(int, sys.stdin.readline().split())
    board, points = [], []
    ans = 0
    for i in range(N):
        board.append(sys.stdin.readline()[:M])
    for i in range(N):
        for j in range(M):
            points.append([i, j])
    cases = list(product([0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]))
    points = list(permutations(points, 2)) #2개를 골라서 p1, p2를 선정함
    for case in cases:
        tmp = getarea(case)
        if ans < tmp:
            ans = tmp
    print(ans)


def getarea(case):
    global N, M, board, points
    l1, l2 = case[0], case[1]
    flag = 0
    for c in points:
        tmp = setcross(l1, l2, c[0], c[1])
        if tmp != 0:
            flag = 1
            break
    if flag:
        return (1 + l1 * 4) * (1 + l2 * 4)
    else:
        return 0


def setcross(l1, l2, p1, p2):
    global N, M, board
    visit = [[0 for j in range(M)] for i in range(N)]
    y1, x1 = p1[0], p1[1]
    y2, x2 = p2[0], p2[1]
    if (0 <= y1 + l1 < N and 0 <= x1 + l1 < M and 0 <= y1 - l1 < N and 0 <= x1 - l1 < M) and 0 <= y2 + l2 < N and 0 <= x2 + l2 < M and 0 <= y2 - l2 < N and 0 <= x2 - l2 < M:
        for i in range(y1 - l1, y1 + l1 + 1):
            if board[i][x1] == '#':
                visit[i][x1] = 1
            else:
                return 0
        for j in range(x1 - l1, x1 + l1 + 1):
            if board[y1][j] == '#':
                visit[y1][j] = 1
            else:
                return 0
        for i in range(y2 - l2, y2 + l2 + 1):
            if board[i][x2] == '#' and visit[i][x2] == 0:
                visit[i][x2] = 1
            else:
                return 0
        for j in range(x2 - l2, x2 + l2 + 1):
            if j == x2:
                continue
            else:
                if board[y2][j] == '#' and visit[y2][j] == 0:
                    visit[y2][j] = 1
                else:
                    return 0
    else:
        return 0
    return 1


if __name__ == '__main__':
    main()
