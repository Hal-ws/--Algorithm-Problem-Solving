import sys
from queue import deque


def main():
    K = int(sys.stdin.readline())
    for i in range(K):
        V, E = map(int, sys.stdin.readline().split())
        matrix = [[0 for j in range(V + 1)] for k in range(V + 1)]
        color = [0] * (V + 1)
        for j in range(E):
            a, b = map(int, sys.stdin.readline().split())
            matrix[a][b] = 1
            matrix[b][a] = 1
        print(bfs(matrix, color, V)) # 1번 정점부터 시작해서 순회 시작


def bfs(matrix, color, V):
    visitChk = [0] * (V + 1)
    q = deque()
    q.append(1)
    color[1] = 1 ## 1: white, 2: black
    visitChk[1] = 1
    while len(q) > 0:
        for i in range(1, V + 1):
            if matrix[q[0]][i] == 1: ## 연결된 간선 탐색
                if visitChk[i] == 0: ## 방문 안했을 시에는 색깔 칠한다
                    if color[q[0]] == 1:
                        color[i] = 2
                    else:
                        color[i] = 1
                    visitChk[i] = 1
                    q.append(i)
                else: ## 이미 방문한 곳일때
                    if color[q[0]] == color[i]:
                        return "NO"
        del q[0]
    return "YES"


if __name__ == "__main__":
    main()
