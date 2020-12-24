import sys
from _collections import deque

def main():
    global N
    N = int(sys.stdin.readline())
    matrix = []
    answer = []
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        answer.append(bfs(matrix, i))
    for i in range(N):
        for j in range(N):
            print(answer[i][j], end=' ')
        print()

def bfs(matrix, start):
    global N
    visit = [0] * N #방문가능한 곳 확인
    q = deque()
    visit[start] = 1
    q.append(start)
    while len(q) > 0:
        cur = q[0]
        for j in range(N):
            if matrix[cur][j] == 1:
                if j == start:
                    visit[start] = 2 # 자기자신으로 돌아오는것 가능
                else:
                    if visit[j] == 0:
                        visit[j] = 1
                        q.append(j)
        q.popleft()
    if visit[start] == 2:
        visit[start] = 1
    else:
        visit[start] = 0
    return visit


if __name__ == '__main__':
    main()
