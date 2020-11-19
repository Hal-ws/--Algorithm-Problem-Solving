import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    board = [[0 for i in range(N + 1)] for j in range(N + 1)]
    board[1][1] = 4
    K = int(sys.stdin.readline())
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        board[a][b] = 9 # 사과
    L = int(sys.stdin.readline())
    changes = []
    for i in range(L):
        a, b = map(str, sys.stdin.readline().split())
        a = int(a)
        changes.append([a, b])
    snake = deque()
    snake.append([1, 1])
    length = 1
    direction = 1 # 위쪽: 0, 오른쪽: 1, 아래쪽: 2, 왼쪽: 3
    timeIdx = 0
    time = 0
    while 1:
        if timeIdx < L:
            if time == changes[timeIdx][0]:
                direction = turn(direction, changes[timeIdx][1])
                timeIdx += 1
        a = movingsnake(board, snake, direction, length, N)
        time += 1
        if a == 0:
            break
        if a == 1:
            length += 1
    print(time)


def turn(before, order):
    if order == "D":
        if before < 3:
            return before + 1
        else:
            return 0
    else:
        if before > 0:
            return before - 1
        else:
            return 3


def movingsnake(board, snake, direction, length, N): # head의 행, 렬 좌표: snake[0][0], snake[0][1]
    head = snake[0]
    tail = snake[length - 1]
    if direction == 0: #위로감
        if head[0] == 1 or board[head[0] - 1][head[1]] == 4:
            return 0
        snake.appendleft([head[0] - 1, head[1]])
        if board[head[0] - 1][head[1]] == 9: #사과먹음
            board[head[0] - 1][head[1]] = 4
            return 1
        else:
            board[head[0] - 1][head[1]] = 4
            board[tail[0]][tail[1]] = 0
            snake.pop()
            return 2
    if direction == 1: #오른쪽으로감
        if head[1] == N or board[head[0]][head[1] + 1] == 4:
            return 0
        snake.appendleft([head[0], head[1] + 1])
        if board[head[0]][head[1] + 1] == 9:
            board[head[0]][head[1] + 1] = 4
            return 1
        else:
            board[head[0]][head[1] + 1] = 4
            board[tail[0]][tail[1]] = 0
            snake.pop()
            return 2
    if direction == 2: #아래쪽
        if head[0] == N or board[head[0] + 1][head[1]] == 4:
            return 0
        snake.appendleft([head[0] + 1, head[1]])
        if board[head[0] + 1][head[1]] == 9:
            board[head[0] + 1][head[1]] = 4
            return 1
        else:
            board[head[0] + 1][head[1]] = 4
            board[tail[0]][tail[1]] = 0
            snake.pop()
            return 2
    if direction == 3: #왼쪽
        if head[1] == 1 or board[head[0]][head[1] - 1] == 4:
            return 0
        snake.appendleft([head[0], head[1] - 1])
        if board[head[0]][head[1] - 1] == 9:
            board[head[0]][head[1] - 1] = 4
            return 1
        else:
            board[head[0]][head[1] - 1] = 4
            board[tail[0]][tail[1]] = 0
            snake.pop()
            return 2


if __name__ == "__main__":
    main()
