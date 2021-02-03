import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    visit = [0] * (N + 1)
    connect = [[] for i in range(N + 1)]
    relate = [[0, [], 0, 0] for i in range(N + 1)] # 부모 노드, 자식 노드, 자식 노드의 수, dfs 에서 cnt 한 자식 노드의 수
    for i in range(1, N):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
        connect[b].append(a)
    nList = list(map(int, sys.stdin.readline().split()))
    q = deque()
    q.append(1)
    visit[1] = 1
    while len(q) > 0:
        c = q[0]
        for nxt in connect[c]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                relate[c][1].append(nxt)
                relate[c][2] += 1
                relate[nxt][0] = c
                q.append(nxt)
        q.popleft()
    if nList[0] != 1: #1이 아닌걸로 시작하면
        print(0)
        return
    stack = [1]
    for i in range(1, N):
        c = nList[i]
        p = stack[-1]
        if relate[c][0] == p: # p 가 c의 부모임
            if relate[c][2] > 0:
                stack.append(c)
            relate[p][3] += 1
        else:
            print(0)
            return
        while 1:
            if len(stack) == 0:
                break
            if relate[stack[-1]][3] == relate[stack[-1]][2]:
                stack.pop()
            else:
                break
    print(1)
    return


if __name__ == '__main__':
    main()
