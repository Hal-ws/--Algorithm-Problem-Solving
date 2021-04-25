import sys
from collections import deque


def main():
    M, N, H = map(int, sys.stdin.readline().split())
    box = [[[0 for j in range(M)] for i in range(N)] for k in range(H)]
    visit = [[[0 for j in range(M)] for i in range(N)] for k in range(H)]
    dz = [-1, 0, 0, 0, 0, 1]
    dy = [0, -1, 1, 0, 0, 0]
    dx = [0, 0, 0, -1, 1, 0]
    q = deque()
    maxT = 0
    for k in range(H):
        for i in range(N):
            tmp = list(map(int, sys.stdin.readline().split()))
            for j in range(M):
                box[k][i][j] = tmp[j]
                if tmp[j] == 1:
                    q.append([k, i, j, 0]) # 좌표, t
    while len(q) > 0:
        tmp = q.popleft()
        z, y, x, t = tmp[0], tmp[1], tmp[2], tmp[3]
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and box[nz][ny][nx] == 0 and visit[nz][ny][nx] == 0:
                visit[nz][ny][nx] = t + 1
                q.append([nz, ny, nx, t + 1])
                box[nz][ny][nx] = 1
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if box[k][i][j] == 0: # 안익은거 남아있음
                    print(-1)
                    return
                if box[k][i][j] and visit[k][i][j] > maxT:
                    maxT = visit[k][i][j]
    print(maxT)


if __name__ == '__main__':
    main()
