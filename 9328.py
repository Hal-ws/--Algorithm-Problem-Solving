import sys
from collections import deque


def main():
    global board, h, w, ans, dy, dx
    T = int(sys.stdin.readline())
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for _ in range(T):
        h, w = map(int, sys.stdin.readline().split())
        ans = 0
        board = []
        for i in range(h):
            board.append(list(sys.stdin.readline()[:w]))
        iniKey = sys.stdin.readline()
        iniKey = iniKey[:len(iniKey) - 1]
        if iniKey != '0':
            key = [0] * 26
            for k in iniKey:
                key[ord(k) - 97] = 1
        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    if board[i][j] == '.':
                        getChk = [[0 for j in range(w)] for i in range(h)]
                        bfs([i, j], key, 0, getChk)
                    elif board[i][j] == '$':
                        getChk = [[0 for j in range(w)] for i in range(h)]
                        getChk[i][j] = 1
                        bfs([i, j], key, 1, getChk)
                    elif board[i][j] != '*':
                        c = board[i][j]
                        getChk = [[0 for j in range(w)] for i in range(h)]
                        if 65 <= ord(c) <= 90: # 대문자일때
                            if key[ord(c) - 65]: # 열쇠가 있을때
                                bfs([i, j], key, 0, getChk)
                        else:
                            key[ord(c) - 97] = 1
                            bfs([i, j], key, 0, getChk)
                            key[ord(c) - 97] = 0
        print(ans)


def bfs(start, key, cnt, getChk):
    global board, h, w, ans, dy, dx
    visit = [[0 for j in range(w)] for i in range(h)]
    visit[start[0]][start[1]] = 1
    q = deque()
    q.append(start)
    newKey = [key[i] for i in range(26)]
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0 and board[ny][nx] != '*':
                if board[ny][nx] != '.':
                    if board[ny][nx] == '$':
                        visit[ny][nx] = 1
                        getChk[ny][nx] = 1
                        cnt += 1
                    else:
                        if 65 <= ord(board[ny][nx]) <= 90:
                            if key[ord(board[ny][nx]) - 65]: #키를 갖고 있을때
                else:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt, newKey])


    return 0


if __name__ == '__main__':
    main()
