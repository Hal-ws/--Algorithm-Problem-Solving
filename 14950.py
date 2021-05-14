import sys


def main():
    global roots
    N, M, t = map(int, sys.stdin.readline().split())
    roads = []
    roots = [i for i in range(N + 1)] # 0번은 더미
    ans = 0
    cnt = 0
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        roads.append([c, a, b])
    roads.sort()
    for i in range(M):
        c, a, b = roads[i][0], roads[i][1], roads[i][2]
        root1, root2 = find(a), find(b)
        if root1 != root2:
            union(root1, root2)
            cnt += 1
            ans += c
    ans = ans + (t * cnt * (cnt - 1) // 2)
    print(ans)


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
        roots[root1] = root2


if __name__ == '__main__':
    main()
