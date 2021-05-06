import sys
from collections import deque


def main():
    global relations, leavesCnt
    N, R, Q = map(int, sys.stdin.readline().split())
    q = deque()
    sys.setrecursionlimit(pow(10, 6))
    relations = [[None, []] for i in range(N + 1)] # 부모, 자식
    connect = [[] for i in range(N + 1)]
    visit = [0 for j in range(N + 1)]
    leavesCnt = [0 for i in range(N + 1)]
    for i in range(N - 1):
        U, V = map(int, sys.stdin.readline().split())
        connect[U].append(V)
        connect[V].append(U)
    q.append(R) # root부터 시작
    visit[R] = 1
    while len(q) > 0:
        curNode = q.popleft()
        for nxtNode in connect[curNode]:
            if visit[nxtNode] == 0:
                visit[nxtNode] = 1
                relations[curNode][1].append(nxtNode)
                relations[nxtNode][0] = curNode
                q.append(nxtNode)
    getLeaves(R)
    for i in range(Q):
        U = int(sys.stdin.readline())
        print(leavesCnt[U])
    
    
def getLeaves(root):
    global relations, leavesCnt
    cnt = 0
    for nxtNode in relations[root][1]:
        cnt += getLeaves(nxtNode)
    leavesCnt[root] = cnt + 1
    return cnt + 1


if __name__ == '__main__':
    main()
