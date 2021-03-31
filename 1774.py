import sys
from math import sqrt


def main():
    global roots
    N, M = map(int, sys.stdin.readline().split())
    pos = [[None, None]]
    roots = [i for i in range(N + 1)]
    roads = []
    answer = 0
    for i in range(N):
        pos.append(list(map(int, sys.stdin.readline().split())))
    for i in range(M):
        p1, p2 = map(int, sys.stdin.readline().split())
        union(p1, p2)
    for node1 in range(1, N):
        for node2 in range(node1 + 1, N + 1):
            dis = getdis(pos[node1], pos[node2])
            roads.append([dis, node1, node2])
    roads.sort()
    for road in roads:
        dis, node1, node2 = road[0], road[1], road[2]
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            union(root1, root2)
            answer += dis
    print(format(answer, ".2f"))


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = roots[root1]


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]


def getdis(node1, node2):
    x1, y1 = node1[0], node1[1]
    x2, y2 = node2[0], node2[1]
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


if __name__ == '__main__':
    main()
