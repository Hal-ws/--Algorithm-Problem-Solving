import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        print(findcommonroot())
    return 0


def findcommonroot():
    N = int(sys.stdin.readline())
    tree = [None] * (N + 1) # idx node의 root 표시
    rootChk = [0] * (N + 1)
    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        tree[B] = A
    node1, node2 = map(int, sys.stdin.readline().split())
    rootChk[node1], rootChk[node2] = 1, 1
    while 1:
        root1 = tree[node1]
        if root1 == None:
            break
        rootChk[root1] += 1
        node1 = root1
    while 1:
        root2 = tree[node2]
        if root2 == None:
            break
        rootChk[root2] += 1
        if rootChk[root2] == 2:
            return root2
        node2 = root2


if __name__=="__main__":
    main()
