import sys
from _collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    inDegree = [0 for i in range(N + 1)]
    connect = [[] for i in range(N + 1)]
    answer = []
    q = deque()
    for _ in range(M):
        tList = list(map(int, sys.stdin.readline().split()))
        tList = tList[1:]
        for i in range(len(tList) - 1):
            cur, nxt = tList[i], tList[i + 1]
            connect[cur].append(nxt)
            inDegree[nxt] += 1
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
    while len(q) > 0:
        cur = q.popleft()
        for nxt in connect[cur]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                q.append(nxt)
        answer.append(cur)
    if len(answer) == N:
        for i in range(N):
            print(answer[i])
    else:
        print(0)


if __name__ == '__main__':
    main()
