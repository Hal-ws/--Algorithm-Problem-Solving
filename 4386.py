import sys
from math import sqrt


def main():
    global roots
    n = int(sys.stdin.readline())
    stars = []
    starDis = []
    roots = [i for i in range(n)]
    answer = 0
    for i in range(n):
        stars.append(list(map(float, sys.stdin.readline().split())))
    for i in range(n - 1):
        for j in range(i + 1, n):
            s1, s2 = stars[i], stars[j]
            d = sqrt(pow(s2[0] - s1[0], 2) + pow(s2[1] - s1[1], 2))
            starDis.append([d, i, j])
    starDis.sort()
    for c in starDis:
        d, n1, n2 = c[0], c[1], c[2]
        if find(n1) != find(n2):
            answer += d
            union(n1, n2)
    print(answer)


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root1] = root2


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]


if __name__ == '__main__':
    main()
