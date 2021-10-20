import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    board = [[0 for j in range(N)] for i in range(N)]
    for i in range(K):
        y, x = map(int, sys.stdin.readline().split())
        board[y - 1][x - 1] = 2  # 사과는 2로 표시
    L = int(sys.stdin.readline())
    snake = deque()
    turnQueue = deque()
    for i in range(L):
        a, b = map(str, sys.stdin.readline().split())
        a = int(a)
        turnQueue.append([a, b])
    t = 0
    board[0][0] = 1  # 뱀은 1로 표시
    snake.append([0, 0])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    d = 1  # 초기에는 오른쪽 향함
    while 1:
        t += 1
        y, x = snake[0][0], snake[0][1]
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1:
            snake.appendleft([ny, nx])
            if board[ny][nx] == 0:  # 빈칸으로 갈 때
                tail = snake.pop()
                board[tail[0]][tail[1]] = 0
            board[ny][nx] = 1
        else:
            print(t)
            break
        if len(turnQueue) > 0 and t == turnQueue[0][0]:  # 방향전환 해야함
            tmp = turnQueue.popleft()
            if tmp[1] == 'D':  #오른쪽으로 꺾음
                d = (d + 1) % 4
            else:
                d -= 1
                if d == -1:
                    d = 3


if __name__ == "__main__":
    main()
