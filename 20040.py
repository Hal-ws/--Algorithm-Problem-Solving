import sys


def main():
    global roots
    n, m = map(int, sys.stdin.readline().split())
    roots = [i for i in range(n)] # i번 node의 root 저장
    ans = 0
    for t in range(1, m + 1):
        a, b = map(int, sys.stdin.readline().split())
        if find(a) == find(b):
            ans = t
            break
        else:
            union(a, b)
    print(ans)


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


def find(node):
    global roots
    if roots[node] == node:
        return node
    tmp = find(roots[node])
    roots[node] = tmp
    return tmp


if __name__ == '__main__':
    main()
