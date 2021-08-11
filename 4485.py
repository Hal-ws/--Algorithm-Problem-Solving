import sys
import heapq
from math import inf


def main():
    t = 1
    while 1:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        ans = getMinLossMoney(N)
        print("Problem %s: %s" %(t, ans))
        t += 1


def getMinLossMoney(N):
    board = []
    visit = [[inf for j in range(N)] for i in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    hq = []
    heapq.heappush(hq, [board[0][0], 0, 0])
    visit[0][0] = board[0][0]
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cMoney, y, x = tmp[0], tmp[1], tmp[2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                tMoney = cMoney + board[ny][nx]
                if tMoney < visit[ny][nx]:
                    visit[ny][nx] = tMoney
                    heapq.heappush(hq, [tMoney, ny, nx])
    return visit[N - 1][N - 1]


if __name__ == "__main__":
    main()
