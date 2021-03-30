import sys


def main():
    global roots
    N, M = map(int, sys.stdin.readline().split())
    maxCost = 0
    totalCost = 0
    roads = []
    roots = [i for i in range(N + 1)]
    for i in range(M):
        p1, p2, cost = map(int, sys.stdin.readline().split())
        roads.append([cost, p1, p2])
    roads.sort()
    for road in roads:
        cost, p1, p2 = road[0], road[1], road[2]
        root1, root2 = find(p1), find(p2)
        if root1 != root2:
            union(root1, root2)
            totalCost += cost
            if maxCost < cost:
                maxCost = cost
    print(totalCost- maxCost)


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]


if __name__ == '__main__':
    main()
