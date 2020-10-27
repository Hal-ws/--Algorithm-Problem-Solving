import sys
from collections import deque


def main():
    K = int(sys.stdin.readline())
    for i in range(K):
        V, E = map(int, sys.stdin.readline().split())
        connect = [[j] for j in range(V + 1)]
        color = [0] * (V + 1)
        for j in range(E):
            a, b = map(int, sys.stdin.readline().split())
            connect[a].append(b)
            connect[b].append(a)
        visitChk = [0] * (V + 1) #0번 idx에는 방문한 노드의 총 개수 저장
        for j in range(1, V + 1):
            if visitChk[j] == 0:
                ans = bfs(connect, color, visitChk, j, V)
            if ans == "NO" or ans == "YES":
                print(ans)
                break



def bfs(connect, color, visitChk, start, V):
    q = deque()
    q.append(start)
    color[start] = 1 ## 1: white, 2: black
    visitChk[start] = 1
    visitChk[0] += 1
    while len(q) > 0:
        l = len(connect[q[0]])
        for i in range(1, l):
            if visitChk[connect[q[0]][i]] == 0: ## 방문 안했을 시에는 색깔 칠한다
                if color[q[0]] == 1:
                    color[connect[q[0]][i]] = 2
                else:
                    color[connect[q[0]][i]] = 1
                visitChk[connect[q[0]][i]] = 1
                visitChk[0] += 1
                q.append(connect[q[0]][i])
            else: ## 이미 방문한 곳일때
                if color[connect[q[0]][0]] == color[connect[q[0]][i]]:
                    return "NO"
        del q[0]
    if visitChk[0] == V:
        return "YES"


if __name__ == "__main__":
    main()
