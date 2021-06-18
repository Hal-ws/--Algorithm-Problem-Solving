import sys
from _collections import deque
from math import inf


def main():
    global h, w, minK, p, visitCnt, board, ansBoard
    T = int(sys.stdin.readline())
    for _ in range(T):
        h, w = map(int, sys.stdin.readline().split())
        board = [['.'] * (w + 2)]
        p = []
        for i in range(h):
            board.append(['.'] + list(sys.stdin.readline()[:w]) + ['.'])
            for j in range(w + 2):
                if board[i + 1][j] == '$':
                    p.append([i + 1, j])
        p.append([0, 0])
        board.append(['.'] * (w + 2))
        ansBoard = [[0 for j in range(w + 2)] for i in range(h + 2)]
        # 최소 열쇠 수를 p1, p2, 외부인 이렇게 각각 저장
        visitCnt = [[[0 for j in range(w + 2)] for i in range(h + 2)] for k in range(3)]
        for i in range(3):
            bfs(i)
        answer = inf
        for i in range(h + 2):
            for j in range(w + 2):
                if visitCnt[0][i][j] and visitCnt[1][i][j] and visitCnt[2][i][j]: # 세명 전부다 방문한 기록이 있을때
                    if board[i][j] == '#':
                        if ansBoard[i][j] - 2 < answer:
                            answer = ansBoard[i][j] - 2
                    if board[i][j] == '.':
                        if ansBoard[i][j] < answer:
                            answer = ansBoard[i][j]
        print(answer)


def bfs(i):
    global h, w, minK, p, visitCnt, board, ansBoard
    q = deque()
    visit = [[inf for j in range(w + 2)] for i in range(h + 2)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    person = p[i]
    q.append([person[0], person[1], 0]) # y, x, 연 문의 갯수
    visit[person[0]][person[1]] = 0
    visitCnt[i][person[0]][person[1]] = 1
    while len(q) > 0:
        tmp = q.popleft()
        y, x, cnt = tmp[0], tmp[1], tmp[2]
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2:
                if board[ny][nx] == '.' or board[ny][nx] == '$':
                    if cnt < visit[ny][nx]:
                        visit[ny][nx] = cnt
                        q.append([ny, nx, cnt])
                        visitCnt[i][ny][nx] = 1
                if board[ny][nx] == '#':
                    if cnt + 1 < visit[ny][nx]:
                        visit[ny][nx] = cnt + 1
                        q.append([ny, nx, cnt + 1])
                        visitCnt[i][ny][nx] = 1
    for y in range(h + 2):
        for x in range(w + 2):
            if visitCnt[i][y][x]: # 방문한적이 있을 때
                ansBoard[y][x] += visit[y][x]


if __name__ == '__main__':
    main()
