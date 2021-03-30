import sys
from _collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    inDegree = [0 for i in range(N + 1)]
    connect = [[] for i in range(N + 1)]
    answer = []
    q = deque()
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
        inDegree[b] += 1
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
    while len(q) > 0:
        cur = q.popleft()
        answer.append(cur)
        for nxt in connect[cur]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                q.append(nxt)
    for p in answer:
        print(p, end=' ')


if __name__ == '__main__':
    main()
