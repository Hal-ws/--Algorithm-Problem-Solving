import sys


def main():
    global roots
    V, E = map(int, sys.stdin.readline().split())
    answer = 0
    connect = []
    roots = [i for i in range(V + 1)]
    for i in range(E):
        n1, n2, dis = map(int, sys.stdin.readline().split())
        connect.append([dis, n1, n2])
    connect.sort()
    for e in connect:
        d, n1, n2 = e[0], e[1], e[2]
        if find(n1) != find(n2):
            answer += d
            union(n1, n2)
    print(answer)


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
