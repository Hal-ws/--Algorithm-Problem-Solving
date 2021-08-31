import sys
from collections import deque


def main():
    global N, M, room, area, dy, dx, crash
    M, N = map(int, sys.stdin.readline().split())
    room = []
    area = [[0 for j in range(M)] for i in range(N)]
    crash = [[10000 for j in range(M)] for i in range(N)] #해당 위치에 도착하기 위해 부순 벽돌의 최소 갯수
    q1 = deque()
    q1.append([0, 0, 0])
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline()[:M])))
    bfs([0, 0], 1, q1)
    if area[0][0] == area[N - 1][M - 1]:
        print(0)
        return
    crash[0][0] = 0
    while len(q1) > 0:
        tmp = q1.popleft()
        y, x, cnt = tmp[0], tmp[1], tmp[2]
        if crash[y][x] == cnt:
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if room[ny][nx] == 0: #빈칸일때
                        if cnt < crash[ny][nx]: # 더 적게 부수고 도착할 수 있는 경우라면
                            crash[ny][nx] = cnt
                            q1.append([ny, nx, cnt])
                    else: #벽일때
                        if cnt + 1 < crash[ny][nx]:
                            crash[ny][nx] = cnt + 1
                            q1.append([ny, nx, cnt + 1])
    print(crash[N - 1][M - 1])


def bfs(pos, cnt, q1):
    global N, M, room, area, dy, dx, crash
    visit = [[0 for j in range(M)] for i in range(N)]
    q = deque()
    q.append(pos)
    visit[pos[0]][pos[1]] = 1
    area[pos[0]][pos[1]] = cnt
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and room[ny][nx] == 0:
                q.append([ny, nx])
                visit[ny][nx] = 1
                area[ny][nx] = cnt
                crash[ny][nx] = 0
                q1.append([ny, nx, 0])
        q.popleft()


if __name__ == "__main__":
    main()
