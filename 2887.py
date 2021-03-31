import sys


def main():
    global roots
    N = int(sys.stdin.readline())
    roots = [i for i in range(N)]
    xyz, yxz, zxy = [], [], []
    answer = 0
    for i in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        xyz.append([x, y, z, i])
        yxz.append([y, x, z, i])
        zxy.append([z, x, y, i])
    xyz.sort()
    yxz.sort()
    zxy.sort()
    turnels = []
    for i in range(N - 1):
        p1, p2 = xyz[i], xyz[i + 1]
        dis = abs(p2[0] - p1[0])
        node1, node2 = p1[3], p2[3]
        turnels.append([dis, node1, node2])
    for i in range(N - 1):
        p1, p2 = yxz[i], yxz[i + 1]
        dis = abs(p2[0] - p1[0])
        node1, node2 = p1[3], p2[3]
        turnels.append([dis, node1, node2])
    for i in range(N - 1):
        p1, p2 = zxy[i], zxy[i + 1]
        dis = abs(p2[0] - p1[0])
        node1, node2 = p1[3], p2[3]
        turnels.append([dis, node1, node2])
    turnels.sort()
    for t in turnels:
        dis, n1, n2 = t[0], t[1], t[2]
        root1, root2 = find(n1), find(n2)
        if root1 != root2:
            union(root1, root2)
            answer += dis
    print(answer)


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


if __name__ == '__main__':
    main()
