import sys

sys.setrecursionlimit(pow(10, 8))

def main():
    global parent
    n, m = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n + 1)] # 각 node의 parent 표시
    for i in range(m):
        x, a, b = map(int, sys.stdin.readline().split())
        if x:
            root1, root2 = findRoot(a), findRoot(b)
            if root1 == root2:
                print('YES')
            else:
                print('NO')
        else:
            union(a, b)


def union(node1, node2):
    global parent
    root1, root2 = findRoot(node1), findRoot(node2)
    if root1 != root2: # 다른 union일때 합쳐줌
        parent[root1] = root2


def findRoot(node):
    global parent
    if parent[node] == node:
        return node # 자기자신이 부모면 root임
    tmp = findRoot(parent[node])
    parent[node] = tmp
    return tmp


if __name__ == '__main__':
    main()
