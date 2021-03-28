import sys


def main():
    global roots
    t = 1
    while 1:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break
        roots = [i for i in range(n + 1)]
        trees = set() # trees의 root가 되는것들을 저장
        for i in range(m):
            node1, node2 = map(int, sys.stdin.readline().split())
            root1, root2 = find(node1), find(node2)
            if root1 != -1 and root2 != -1: # 둘다 tree의 root일때
                if root1 != root2: # 서로 다를때
                    union(root1, root2)
                else: # 서로 같을때. 사이클을 이룸
                    roots[root1] = -1
            else:
                if root1 == -1: # root1이 -1일 때
                    roots[root2] = -1
                if root2 == -1:
                    roots[root1] = -1
        for i in range(1, n + 1):
            if roots[i] != -1:
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
        t += 1


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


def find(node):
    global roots
    if roots[node] == node:
        return node
    if roots[node] == -1:
        return -1
    roots[node] = find(roots[node])
    return roots[node]


if __name__ == '__main__':
    main()
