import sys


def main():
    N = int(sys.stdin.readline())
    board = []
    ans = 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    vectorList = []
    vectorList.append([[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 0, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]])
    vectorList.append([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 0, 10, 0], [0, 0, 5, 0, 0]])
    vectorList.append([[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 0, 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]])
    vectorList.append([[0, 0, 5, 0, 0], [0, 10, 0, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]])
    y, x = N // 2, N // 2
    d = 1
    while 1:
        for j in range(d):
            x -= 1
            ans += tornado(board, y, x, 0, N, vectorList)
            if y == 0 and x == 0:
                print(ans)
                return
        for i in range(d):
            y += 1
            ans += tornado(board, y, x, 1, N, vectorList)
        d += 1
        for j in range(d):
            x += 1
            ans += tornado(board, y, x, 2, N, vectorList)
        for i in range(d):
            y -= 1
            ans += tornado(board, y, x, 3, N, vectorList)
        d += 1


def tornado(board, y, x, d, N, vectorList):   # d: 0, 1, 2, 3 -> 좌, 하, 우, 상
    useVector = vectorList[d]  # 사용할 벡터
    sand = board[y][x]  # y, x 에 있는 sand들이 이동
    result = 0
    mvSum = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            ny, nx = y + i, x + j
            moveSand = int(sand * (useVector[i + 2][j + 2] / 100))
            if 0 <= ny < N and 0 <= nx < N:  # 해당 모래가 이동
                board[ny][nx] += moveSand
            else:  # board 바깥으로 나감
                result += moveSand
            board[y][x] = 0
            mvSum += moveSand
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    ny, nx = y + dy[d], x + dx[d]  # a의 위치
    if 0 <= ny < N and 0 <= nx < N: #
        board[ny][nx] += (sand - mvSum)
    else:
        result += (sand - mvSum)
    return result


if __name__ == "__main__":
    main()
