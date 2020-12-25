from collections import deque
import sys


def main():
    M, N, H = map(int, sys.stdin.readline().split())
    box = []
    for k in range(H):
        layer = []
        for i in range(N):
            layer.append(list(map(int, sys.stdin.readline().split())))
        box.append(layer)
    q = deque()
    visited = [[[0 for j in range(M)] for i in range(N)] for k in range(H)]
    cnt = 0 # 안익은 토마토 셈
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if box[k][i][j] == 1:
                    q.append([k, i, j, 0])
                    visited[k][i][j] = 1
                if box[k][i][j] == 0:
                    cnt += 1
    if cnt == 0:
        print(0)
        return
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    while 1:
        curz, cury, curx, day = q[0][0], q[0][1], q[0][2], q[0][3]
        for i in range(6):
            nz, ny, nx = curz + dz[i], cury + dy[i], curx + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if box[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                    q.append([nz, ny, nx, day + 1])
                    visited[nz][ny][nx] = 1
                    cnt -= 1
        q.popleft()
        if len(q) == 0:
            answer = day
            break
    if cnt == 0:
        print(answer)
    else:
        print(-1)


if __name__ == '__main__':
    main()
