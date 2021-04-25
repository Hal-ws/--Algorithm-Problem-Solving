import sys


def main():
    global roots
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    connect = []
    answer = 0
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        connect.append([c, a - 1, b - 1])
    connect.sort()
    roots = [i for i in range(N)]
    for tmp in connect:
        price, a, b = tmp[0], tmp[1], tmp[2]
        root1, root2 = find(a), find(b)
        if root1 != root2:
            answer += price
            union(root1, root2)
    print(answer)


def find(node):
    global roots
    if roots[node] == node:
        return node
    root = find(roots[node])
    roots[node] = root
    return root


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = roots[root1]


if __name__ == '__main__':
    main()
