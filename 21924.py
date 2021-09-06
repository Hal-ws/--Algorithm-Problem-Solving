import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    roots = [i for i in range(N + 1)]
    roads = []
    maxCost = 0
    minCost = 0
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        roads.append([c, a, b])  # c의 비용으로 a, b 도시 연결
        maxCost += c
    roads.sort()
    for i in range(M):
        cost, node1, node2 = roads[i][0], roads[i][1], roads[i][2]
        root1, root2 = find(roots, node1), find(roots, node2)
        if root1 != root2:
            union(roots, node1, node2)
            minCost += cost
    stdRoot = find(roots, 1)
    for i in range(2, N + 1):
        if find(roots, i) != stdRoot:
            print(-1)
            return
    print(maxCost - minCost)


def find(roots, node):
    if roots[node] != node:
        roots[node] = find(roots, roots[node])
    return roots[node]


def union(roots, node1, node2):
    root1, root2 = find(roots, node1), find(roots, node2)
    if root1 != root2:
        roots[root2] = root1


if __name__ == "__main__":
    main()
