import sys
from queue import PriorityQueue


def main():
    global connect, n
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    connect = [[] for i in range(n + 1)]
    for i in range(m):
        s, e, p = map(int, sys.stdin.readline().split())
        connect[s].append([e, p])
    start, target = map(int, sys.stdin.readline().split())
    daik(start, target)


def daik(start, target):
    global connect, n
    visit = [-1] * (n + 1)
    q = PriorityQueue()
    visit[start] = 0
    q.put([0, start, str(start)]) # 가격 합, 현재 위치, path
    ansPath = None
    while q.empty() != True:
        tmp = q.get()
        curP, curN, curPath = tmp[0], tmp[1], tmp[2]
        for nxt in connect[curN]:
            nxtNode, tPrice = nxt[0], nxt[1] + curP
            nPath = curPath + ' ' + str(nxtNode)
            if visit[nxtNode] == -1 or tPrice < visit[nxtNode]:
                visit[nxtNode] = tPrice
                if nxtNode == target: # target에 갈때
                    ansPath = nPath
                else:
                    q.put([tPrice, nxtNode, nPath])
    print(visit[target])
    print(ansPath.count(' ') + 1)
    print(ansPath)


if __name__ == '__main__':
    main()
