import sys
from collections import deque


def main():
    global h, w, board, dy, dx, ans
    T = int(sys.stdin.readline())
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for _ in range(T):
        board = []
        h, w = map(int, sys.stdin.readline().split())
        board.append(['.'] * (w + 2))
        for i in range(h):
            board.append(['.'] + list(sys.stdin.readline()[:w]) + ['.'])
        board.append(['.'] * (w + 2))
        h, w = h + 2, w + 2
        iniKey = sys.stdin.readline()
        key = [0] * 26
        ans = 0
        if iniKey[0] != '0':
            for i in range(len(iniKey) - 1):
                key[ord(iniKey[i]) - 97] = 1
        bfs([0, 0], 0, key)
        print(ans)


def bfs(start, cnt, key): #위치, 훔친 문서 수, 갖고 있는 key
    global h, w, board, dy, dx, ans
    if ans < cnt:
        ans = cnt
    visit = [[0 for j in range(w)] for i in range(h)]
    visit[start[0]][start[1]] = 1
    q = deque()
    q.append(start)
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] != '*' and visit[ny][nx] == 0:
                bNum = ord(board[ny][nx])
                if bNum == 46:
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                if 65 <= bNum <= 90 and key[bNum - 65]: # 문을 만났을때
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                if 97 <= bNum <= 122: # 열쇠
                    key[bNum - 97] = 1
                    board[ny][nx] = '.'
                    bfs([ny, nx], cnt, key)
                    key[bNum - 97] = 0
                    board[ny][nx] = chr(bNum)
                if bNum == 36: # 문서 get
                    board[ny][nx] = '.'
                    bfs([ny, nx], cnt + 1, key)
                    board[ny][nx] = chr(bNum)
        q.popleft()


if __name__ == '__main__':
    main()
