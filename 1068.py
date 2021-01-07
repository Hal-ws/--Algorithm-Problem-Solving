import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split())) # 각 node의 부모 노드 정보
    delNode = int(sys.stdin.readline())
    q = deque()
    link = [[] for i in range(N)] #해당 node의 자식nodes 기록
    cnt = 0
    root = None
    for i in range(N):
        parent = parents[i]
        if parent == -1:
            root = i
        if i != delNode and i != root and parent != delNode:
            link[parent].append(i)
    q.append(link[root])
    while len(q) > 0:
        child = q[0]
        for nxt in child:
            q.append(link[nxt])
            if link[nxt] == []:
                cnt += 1
        q.popleft()
    if root != delNode and link[root] == []:
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
