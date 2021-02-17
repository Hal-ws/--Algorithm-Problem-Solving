import sys
from collections import deque


def main():
    global N, M, K, board
    N, M, K = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    print(bfs())


def bfs():
    global N, M, K, board
    dy, dx = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]
    visit = [[[[0 for j in range(M)] for i in range(N)] for k in range(K + 1)] for l in range(2)]
    visit[0][K][0][0] = 1
    q = deque()
    q.append([0, K, 0, 0, 1]) #밤낮, 부술수 있는벽, y, x, 방문 칸 수
    while len(q) > 0:
        time, possK, y, x, cnt = q[0][0], q[0][1], q[0][2], q[0][3], q[0][4]
        if y == N - 1 and x == M - 1:
            return cnt
        if time == 0: # 낮일때
            for i in range(4): # 멈춰있을 이유 없음
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if board[ny][nx] == '1' and 0 < possK: #벽을 부수고 갈때
                        if visit[1][possK - 1][ny][nx] == 0:
                            visit[1][possK - 1][ny][nx] = cnt + 1
                            q.append([1, possK - 1, ny, nx, cnt + 1])
                        elif cnt + 1 < visit[1][possK - 1][ny][nx]:
                            visit[1][possK - 1][ny][nx] = cnt + 1
                            q.append([1, possK - 1, ny, nx, cnt + 1])
                    if board[ny][nx] == '0': # 안부수고 이동가능
                        if visit[1][possK][ny][nx] == 0:
                            visit[1][possK][ny][nx] = cnt + 1
                            q.append([1, possK, ny, nx, cnt + 1])
                        elif cnt + 1 < visit[1][possK][ny][nx]:
                            visit[1][possK][ny][nx] = cnt + 1
                            q.append([1, possK, ny, nx, cnt + 1])
        else: # 밤일때
            for i in range(5): # 멈추고 가는게 나을수도 있음
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if board[ny][nx] == '0': # 벽으로는 못감
                        if visit[0][possK][ny][nx] == 0:
                            visit[0][possK][ny][nx] = cnt + 1
                            q.append([0, possK, ny, nx, cnt + 1])
                        elif cnt + 1 < visit[0][possK][ny][nx]:
                            visit[0][possK][ny][nx] = cnt + 1
                            q.append([0, possK, ny, nx, cnt + 1])
                    else: #벽일때
                        if ny == y and nx == x:
                            if visit[0][possK][ny][nx] == 0:
                                visit[0][possK][ny][nx] = cnt + 1
                                q.append([0, possK, ny, nx, cnt + 1])
                            elif cnt + 1 < visit[0][possK][ny][nx]:
                                visit[0][possK][ny][nx] = cnt + 1
                                q.append([0, possK, ny, nx, cnt + 1])
        q.popleft()
    return - 1


if __name__ == '__main__':
    main()
