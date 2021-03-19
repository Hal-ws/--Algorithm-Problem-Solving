import sys


def main():
    global rootDic, numDic
    T = int(sys.stdin.readline())
    for t in range(T):
        F = int(sys.stdin.readline())
        rootDic = {} # key(이름)이 들어가는 트리의 root 저장
        numDic = {} # key(이름)이 있는 트리에 있는 사람 수 저장
        for i in range(F):
            a, b = map(str, sys.stdin.readline().split())
            if a not in rootDic:
                rootDic[a] = a
                numDic[a] = 1
            if b not in rootDic:
                rootDic[b] = b
                numDic[b] = 1
            union(a, b)
            print(numDic[rootDic[a]])


def union(node1, node2):
    global rootDic, numDic
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        rootDic[root2] = root1
        numDic[root1] += numDic[root2]


def find(node):
    global rootDic
    if rootDic[node] == node:
        return node
    tmp = find(rootDic[node])
    rootDic[node] = tmp
    return tmp


if __name__ == '__main__':
    main()
