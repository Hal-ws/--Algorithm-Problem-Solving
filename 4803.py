import sys


def main():
    global roots
    t = 0
    while 1:
        n, m = map(int, sys.stdin.readline().split())
        t += 1
        if n == 0 and m == 0:
            break
        roots = [i for i in range(n + 1)]
        trees = set() # trees의 root가 되는것들을 저장
        for _ in range(m):
            node1, node2 = map(int, sys.stdin.readline().split())
            root1, root2 = find(node1), find(node2)
            if root1 != -1 and root2 != -1: # 둘다 tree의 root일때
                if root1 != root2: # 서로 다를때
                    union(root1, root2)
                else: # 서로 같을때. 사이클을 이룸
                    roots[root1] = -1
                    roots[root2] = -1
            else: # cycle의 node를 골랐을 때
                if root1 == -1 and root2 != -1:
                    roots[root2] = -1
                if root1 != -1 and root2 == -1:
                    roots[root1] = -1
        for i in range(1, n + 1):
            root = find(i)
            if root != -1:
                trees.add(root)
        cnt = len(list(trees))
        if cnt == 0:
            print('Case %s: No trees.' %t)
        elif cnt == 1:
            print('Case %s: There is one tree.'%t)
        else:
            print('Case %s: A forest of %s trees.' %(t, cnt))


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


def find(node):
    global roots
    if roots[node] == -1:
        return -1
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]


if __name__ == '__main__':
    main()
