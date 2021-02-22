import sys
from queue import PriorityQueue


def main():
    global N, M, K, goDis, backDis, connect
    N, M, K = map(int, sys.stdin.readline().split())
    goDis = [-1] * (N + 1)
    backDis = [-1] * (N + 1)
    connect = [[] for i in range(N + 1)]
    ans = 0
    for i in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        connect[s].append([e, t])
    for i in range(N):
        if goDis[i] != K:
            if goDis[i] == -1:
                daik(i)
        else:
            daik(i)
    for i in range(1, N + 1):
        tmp = goDis[i] + backDis[i]
        if ans < tmp:
            ans = tmp
    print(ans)


def daik(start):
    global N, M, K, goDis, backDis, connect
    q = PriorityQueue()
    q.put([0, start, [start]]) # 총 거리
    disSum = [-1] * (N + 1)
    disSum[start] = 0
    resultPath = None
    while q.empty() != True:
        tmp = q.get()
        d, cur, path = tmp[0], tmp[1], tmp[2]
        for nxt in range(connect[cur]):
            nNode, tDis = nxt[0], d + nxt[1]
            if disSum[nNode] == -1: # 아직 방문안함
                if nxt == K: # 도착지 왔음
                    resultPath = path + [nxt]
                if goDis[nxt] != -1: # 도착 경로 이미 구해둠
                    disToK = tDis + goDis[nxt]


if __name__ == '__main__':
    main()
