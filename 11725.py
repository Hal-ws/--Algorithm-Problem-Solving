import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    connect = [[] for i in range(N + 1)]
    visit = [0] * (N + 1)
    parent = [0] * (N + 1)
    for i in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
        connect[b].append(a)
    q = deque()
    q.append(1) #q에 1 추가
    visit[1] = 1
    while len(q) > 0:
        node = q[0]
        l = len(connect[node]) # node와 연결된값을 고름
        for i in range(l):
            next = connect[node][i] #다음에 방문할 node
            if visit[next] == 0: #지금 node의 부모 노드로는 안감
                q.append(next)
                parent[next] = node
                visit[next] = 1
        q.popleft()
    for i in range(2, N + 1):
        print(parent[i])


if __name__ == '__main__':
    main()
