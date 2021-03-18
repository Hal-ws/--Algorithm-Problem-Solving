import sys
from _collections import deque


def main():
    global N, matrix, visit
    matrix = []
    flag = 1
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    visit = [0] * N
    plan = list(map(int, sys.stdin.readline().split()))
    for i in range(len(plan)):
        plan[i] -= 1
    bfs(plan[0])
    for i in range(len(plan)):
        if visit[plan[i]] == 0:
            flag = 0
            break
    if flag:
        print('YES')
    else:
        print('NO')


def bfs(start):
    global N, matrix, visit
    q = deque()
    q.append(start)
    visit[start] = 1
    while len(q) > 0:
        cur = q.popleft()
        for i in range(N):
            if matrix[cur][i] and visit[i] == 0:
                visit[i] = 1
                q.append(i)
    return 0


if __name__ == '__main__':
    main()
