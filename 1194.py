import sys
from _collections import deque


def main():
    global N, M, board, dy, dx, ans
    N, M = map(int, sys.stdin.readline().split())
    board = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = -1
    minsik = None
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
        for j in range(M):
            if board[i][j] == '0':
                minsik = [i, j] #민식이 좌표
                board[i][j] = '.'
    key = [0, 0, 0, 0, 0, 0]
    bfs(minsik, key, 0)
    print(ans)


def bfs(start, key, cnt):
    global N, M, board, dy, dx, ans
    if ans != -1 and cnt >= ans:
        return
    q = deque()
    q.append([start[0], start[1], cnt])
    visit = [[0 for j in range(M)] for i in range(N)]
    visit[start[0]][start[1]] = 1
    while len(q) > 0:
        print('q: %s' %q)
        print('key: %s' %key)
        tmp = q.popleft()
        y, x, mCnt = tmp[0], tmp[1], tmp[2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0:
                if board[ny][nx] != '#': # 벽이 아니면 진행
                    iVal = ord(board[ny][nx])
                    visit[ny][nx] = 1
                    if 97 <= iVal <= 102: #key를 찾았을 때
                        if key[iVal - 97] == 0: # 키를 새로 주울 때
                            key[iVal - 97] = 1
                            board[ny][nx] = '.'
                            bfs([ny, nx], key, mCnt + 1)
                            key[iVal - 97] = 0
                            board[ny][nx] = chr(iVal)
                        else: #이미 그 키가 있을 때
                            q.append([ny, nx, mCnt + 1])
                    if 65 <= iVal <= 70: # 문일때
                        if key[iVal - 65]: # 키가 있을 때
                            q.append([ny, nx, mCnt + 1])
                    if iVal == 46: # 빈칸
                        q.append([ny, nx, mCnt + 1])
                    if iVal == 49:
                        if ans == -1 or mCnt + 1 < ans:
                            ans = mCnt + 1
                        return
        if ans != -1 and cnt >= ans:
            return
    return


if __name__ == '__main__':
    main()
