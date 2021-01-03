import sys
from collections import deque
from itertools import combinations


def main():
    global N, M, D, board, ans
    board = []
    N, M, D = map(int, sys.stdin.readline().split())
    ans = 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    board.append([2] * M)
    pos = [i for i in range(M)]
    cases = list(combinations(pos, 3))
    for case in cases:
        turn(case)
    print(ans)


def turn(case):
    global N, M, D, board, ans
    tmp = [[0 for j in range(M)] for i in range(N + 1)]
    cnt = 0
    for i in range(N + 1):
        for j in range(M):
            tmp[i][j] = board[i][j]
    while 1:
        cnt += shooting(case, tmp)
        if moving(tmp): #모든 적이 지도에서 다 사라지면
            break
    if ans <= cnt:
        ans = cnt

        
def shooting(case, tmp):
    global N, M, D
    hit = 0
    q = deque()
    visit = [[[0 for j in range(M)] for i in range(N + 1)] for k in range(3)]
    target = []
    findFlag = [0, 0, 0]
    for i in range(3):
        q.append([N, case[i], 0, i])
        visit[i][q[i][0]][q[i][1]] = 1
    dy, dx = [0, -1, 0], [-1, 0, 1]
    while len(q) > 0:
        dis, archer = q[0][2], q[0][3]
        if dis == D:
            q.popleft()
            continue
        for i in range(3):
            ny, nx = q[0][0] + dy[i], q[0][1] + dx[i]
            if 0 <= ny < N + 1 and 0 <= nx < M and visit[archer][ny][nx] == 0:
                visit[archer][ny][nx] = 1
                q.append([ny, nx, dis + 1, archer])
                if tmp[ny][nx] == 1 and findFlag[archer] == 0:
                    target.append([ny, nx])
                    findFlag[archer] = 1
        q.popleft()
    for i in range(len(target)):
        y, x = target[i][0], target[i][1]
        if tmp[y][x] == 1:
            tmp[y][x] = 0
            hit += 1
    return hit


def moving(tmp):
    global N, M
    enemy = 0
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if tmp[i][j] == 1:
                enemy += 1
                if i == N - 1:
                    tmp[i][j] = 0
                    enemy -= 1
                else:
                    tmp[i + 1][j] = 1
                    tmp[i][j] = 0
    if enemy == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()
