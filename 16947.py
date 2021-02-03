import sys
sys.setrecursionlimit(pow(10, 6))
from _collections import deque


def main():
    global N, connection, circle, distance, dfsflag
    N = int(sys.stdin.readline())
    connection = [[] for i in range(N + 1)]
    distance = [-1] * (N + 1)
    dfsflag = 0
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        connection[a].append(b)
        connection[b].append(a)
    visit = [0] * (N + 1)
    for i in range(1, N + 1):
        if visit[i] == 0 and dfsflag == 0:
            visit = [0] * (N + 1)
            visit[i] = 1
            dfs(i, i, None, visit)
            visit[i] = 0
    for i in range(1, N + 1):
        if circle[i] == 1: # circle 의 한 점이면
            ans = bfs(i)
            break
    for i in range(1, N + 1):
        print(ans[i], end=' ')


def dfs(start, cur, before, visit):
    global N, connection, distance, dfsflag, circle
    if dfsflag:
        return
    if before == None:
        for nxt in connection[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                dfs(start, nxt, cur, visit)
                visit[nxt] = 0
    else:
        for nxt in connection[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                dfs(start, nxt, cur, visit)
                visit[nxt] = 0
            else:
                if nxt == start and before != start:
                    dfsflag = 1
                    circle = []
                    for i in range(N + 1):
                        circle.append(visit[i])
                    return

def bfs(node):
    global N, connection, circle, distance
    visit = [0] * (N + 1)
    q = deque()
    q.append([node, 0])
    visit[node] = 1
    distance[node] = 0
    while len(q) > 0:
        cur = q[0][0]
        dis = q[0][1]
        for nxt in connection[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                if circle[nxt]:
                    q.append([nxt, 0])
                    distance[nxt] = 0
                else:
                    q.append([nxt, dis + 1])
                    distance[nxt] = dis + 1
        q.popleft()
    return distance


if __name__ == '__main__':
    main()
