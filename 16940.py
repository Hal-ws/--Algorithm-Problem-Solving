import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    connect = [[] for i in range(N + 1)]
    parent =[[0, [], 0] for i in range(N + 1)] # 부모노드, 자식노드, 자식노드의 수
    visit = [0] * (N + 1)
    q = deque()
    for i in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
        connect[b].append(a)
    nList = list(map(int, sys.stdin.readline().split()))
    q.append([1, 0])
    visit[1] = 1
    while len(q) > 0:
        cur = q[0][0]
        dis = q[0][1]
        for nxt in connect[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                parent[cur][1].append(nxt)
                parent[cur][2] += 1
                parent[nxt][0] = cur
                q.append([nxt, dis + 1])
        q.popleft()
    if nList[0] != 1:
        print(0)
        return
    q = deque()
    q.append(1)
    cnt = 0
    for i in range(1, N):
        p = q[0]
        c = nList[i]
        if parent[c][0] == p: # 부모가 맞을때
            if parent[c][2] > 0:
                q.append(c) 
            cnt += 1
        else: # 부모가 아닐때
            print(0)
            return
        if cnt == parent[p][2]: #자식노드 다 채움
            cnt = 0
            q.popleft()
    print(1)


if __name__ == '__main__':
    main()
