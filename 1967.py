import sys
from sys import setrecursionlimit


def main():
    global n, visit, tree, farnode, ans, dis
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return
    setrecursionlimit(pow(10, 6))
    tree = [[None, []] for i in range(n + 1)]
    for i in range(n - 1):
        p, c, l = map(int, sys.stdin.readline().split())
        tree[p][1].append([c, l])
        tree[c][0] = [p, l]
    dis, farnode, ans = 0, 0, 0 #가장 먼 node, 그 노드로부터 가장 먼 노드의 거리
    visit = [0] * (n + 1)
    visit[1] = 1
    dfs(1, 0)
    visit[1] = 0
    visit = [0] * (n + 1)
    visit[farnode] = 1
    dfs2(farnode, 0)
    visit[farnode] = 0
    print(ans)


def dfs2(node, r):
    global visit, tree, farnode, dis, ans
    flag = 0
    if node != 1:
        p = tree[node][0]
        if visit[p[0]] == 0:
            flag = 1
            visit[p[0]] = 1
            dfs2(p[0], r + p[1])
            visit[p[0]] = 0
    childrens = tree[node][1]
    for nxt in childrens:
        if visit[nxt[0]] == 0:
            flag = 1
            visit[nxt[0]] = 1
            dfs2(nxt[0], r + nxt[1])
            visit[nxt[0]] = 0
    if flag == 0:
        if ans < r:
            ans = r


def dfs(node, r):
    global visit, tree, farnode, dis, ans
    flag = 0
    childs = tree[node][1]
    for nxt in childs:
        cNode, tmpd = nxt[0], nxt[1]
        if visit[cNode] == 0:
            flag = 1
            visit[cNode] = 1
            dfs(cNode, r + tmpd)
            visit[cNode] = 0
    if flag == 0:
        if dis < r:
            dis = r
            farnode = node


if __name__ == '__main__':
    main()
