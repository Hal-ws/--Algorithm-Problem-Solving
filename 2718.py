import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    miro = []
    for i in range(N):
        miro.append(sys.stdin.readline()[:M])
    print(bfs(miro, N, M))

def bfs(miro, N, M):
    visited = [[0 for i in range(M)] for j in range(N)]
    distance = [[0 for i in range(M)] for j in range(N)]
    distance[0][0] = 1
    for i in range(N):
        for j in range(M):
            if miro[i][j] == '1' and visited[i][j] == 0:
                q = [[i, j]]
                visited[i][j] = 1
                while len(q) > 0:
                    if q[0][0] > 0 and miro[q[0][0] - 1][q[0][1]] == '1' and visited[q[0][0] - 1][q[0][1]] == 0:
                        q.append([q[0][0] - 1, q[0][1]])
                        visited[q[0][0] - 1][q[0][1]] = 1
                        distance[q[0][0] - 1][q[0][1]] = distance[q[0][0]][q[0][1]] + 1
                    if q[0][1] < M - 1 and miro[q[0][0]][q[0][1] + 1] == '1' and visited[q[0][0]][q[0][1] + 1] == 0:
                        q.append([q[0][0], q[0][1] + 1])
                        visited[q[0][0]][q[0][1] + 1] = 1
                        distance[q[0][0]][q[0][1] + 1] = distance[q[0][0]][q[0][1]] + 1
                    if q[0][0] < N - 1 and miro[q[0][0] + 1][q[0][1]] == '1' and visited[q[0][0] + 1][q[0][1]] == 0:
                        q.append([q[0][0] + 1, q[0][1]])
                        visited[q[0][0] + 1][q[0][1]] = 1
                        distance[q[0][0] + 1][q[0][1]] = distance[q[0][0]][q[0][1]] + 1
                    if q[0][1] > 0 and miro[q[0][0]][q[0][1] - 1] == '1' and visited[q[0][0]][q[0][1] - 1] == 0:
                        q.append([q[0][0], q[0][1] - 1])
                        visited[q[0][0]][q[0][1] - 1] = 1
                        distance[q[0][0]][q[0][1] - 1] = distance[q[0][0]][q[0][1]] + 1
                    del q[0]
    return distance[N - 1][M - 1]

if __name__ == "__main__":
    main()
