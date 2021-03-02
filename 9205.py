import sys
from collections import deque


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        node = [0] * (n + 2)
        ans = 'sad'
        connect = [[] for i in range(n + 2)] # 각 node별로 도착할 수 있는 node 정리
        visit = [0] * (n + 2)
        for i in range(n + 2):
            node[i] = list(map(int, sys.stdin.readline().split()))
        for i in range(n + 1):
            for j in range(i + 1, n + 2):
                x1, y1 = node[i][0], node[i][1]
                x2, y2 = node[j][0], node[j][1]
                if abs(x2 - x1) + abs(y2 - y1) <= 1000:
                    connect[i].append(j)
                    connect[j].append(i)
        visit[0] = 1
        q = deque()
        q.append(0)
        while len(q) > 0:
            cur = q.popleft()
            if cur == n + 1:
                ans = 'happy'
                break
            for nxt in connect[cur]:
                if visit[nxt] == 0:
                    visit[nxt] = 1
                    q.append(nxt)
        print(ans)


if __name__ == '__main__':
    main()
