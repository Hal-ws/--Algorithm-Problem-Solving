import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    relations = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    matrix = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    print(bfs(matrix, N, relations[0], relations[1]))

def bfs(matrix, N, personA, personB):
    q = deque()
    visited = [0] * (N + 1)
    flag = 0
    visited[personA] = 1
    for i in range(N + 1):
        if matrix[personA][i] == 1:
            q.append(i)
            visited[i] = 1
            if i == personB:
                flag = 1
                break
    distance = 1
    lb = len(q)
    la = len(q)
    if flag == 0:
        while la > 0:
            for i in range(lb): ## q[i]: 지금 q에 쌓여있는 node의 번호
                for j in range(N + 1): ## j: q[i]와 연결된 node의 번호
                    if matrix[q[i]][j] == 1 and visited[j] == 0:
                        if j == personB:
                            return distance + 1
                        q.append(j)
                        visited[j] = 1
                        la += 1
            for j in range(lb):
                q.popleft()
                la -= 1
            lb = la
            distance += 1
    if flag == 0:
        return -1
    else:
        return distance


if __name__ == "__main__":
    main()
