import sys
from collections import deque


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())
        q = deque()
        buildTime = [0] + list(map(int, sys.stdin.readline().split()))
        completeTime = [0 for i in range(N + 1)]
        inDegree = [0 for i in range(N + 1)]
        connect = [[] for i in range(N + 1)]
        for i in range(K):
            a, b = map(int, sys.stdin.readline().split())
            connect[a].append(b)
            inDegree[b] += 1
        W = int(sys.stdin.readline())
        for i in range(1, N + 1):
            if inDegree[i] == 0:
                q.append(i)
                completeTime[i] = buildTime[i]
        while len(q) > 0:
            cur = q.popleft()
            for nxt in connect[cur]:
                inDegree[nxt] -= 1
                totalTime = completeTime[cur] + buildTime[nxt]
                if completeTime[nxt] < totalTime:
                    completeTime[nxt] = totalTime
                if inDegree[nxt] == 0: # 이제 건물 지음
                    q.append(nxt)
        print(completeTime[W])


if __name__ == '__main__':
    main()
