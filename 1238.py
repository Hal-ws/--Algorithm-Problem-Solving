import sys
from queue import PriorityQueue


def main():
    global N, M, K, goDis, backDis, connect, disMatrix
    N, M, K = map(int, sys.stdin.readline().split())
    goDis = [-1] * (N + 1)
    backDis = [-1] * (N + 1)
    disMatrix = [[0 for j in range(N + 1)] for i in range(N + 1)]
    connect = [[] for i in range(N + 1)]
    ans = 0
    for i in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        disMatrix[s][e] = t
        connect[s].append([e, t])
    goDis[K] = 0
    for i in range(1, N + 1):
        if goDis[i] != K:
            if goDis[i] == -1:
                godaik(i)
    backDaik(K)
    for i in range(1, N + 1):
        tmp = goDis[i] + backDis[i]
        if ans < tmp:
            ans = tmp
    print(ans)


def godaik(start):
    global N, M, K, goDis, backDis, connect, disMatrix
    q = PriorityQueue()
    q.put([0, start, [start]])
    disList = [-1] * (N + 1) # start 지점에서 node들까지 갈때 걸린 최소 시간
    disList[start] = 0
    shortPath = None
    shortDis = None
    while q.empty() != True:
        tmp = q.get()
        d, cur, path = tmp[0], tmp[1], tmp[2]
        for nxt in range(len(connect[cur])):
            nNode, tDis = connect[cur][nxt][0], d + connect[cur][nxt][1]
            if disList[nNode] == -1: # 아직 방문안한 노드 방문
                if goDis[nNode] != -1: # 종료조건
                    if shortDis == None or tDis + goDis[nNode] < shortDis: # 아직 최소경로 못구함
                        shortDis = tDis + goDis[nNode]
                        shortPath = path + [nNode]
                else: # 종료조건이 아님
                    disList[nNode] = tDis
                    q.put([tDis, nNode, path + [nNode]])
            else: # 이미 방문한 노드 방문
                if goDis[nNode] != -1: # 종료조건
                    if shortDis == None or tDis + goDis[nNode] < shortDis: # 아직 최소경로 못구함
                        shortDis = tDis + goDis[nNode]
                        shortPath = path + [nNode]
                else: # 계속 탐색해야함
                    if tDis < disList[nNode]:
                        disList[nNode] = tDis
                        q.put([tDis, nNode, path + [nNode]])
    l = len(shortPath)
    for nIdx in range(l):
        node = shortPath[nIdx]
        goDis[node] = shortDis
        if nIdx != l - 1: #맨 끝이 아니면
            shortDis -= disMatrix[node][shortPath[nIdx + 1]]

def backDaik(start):
    global N, M, K, goDis, backDis, connect, disMatrix
    q = PriorityQueue()
    q.put([0, start])
    disList = [-1] * (N + 1) # start 지점에서 node들까지 갈때 걸린 최소 시간
    disList[start] = 0
    while q.empty() != True:
        tmp = q.get()
        d, cur = tmp[0], tmp[1]
        for nIdx in range(len(connect[cur])):
            nxt = connect[cur][nIdx]
            nNode, tDis = nxt[0], d + nxt[1]
            if disList[nNode] == -1: # 아직 방문안함
                disList[nNode] = tDis
                q.put([tDis, nNode])
            elif tDis < disList[nNode]:
                disList[nNode] = tDis
                q.put([tDis, nNode])
    for i in range(1, N + 1):
        backDis[i] = disList[i]


if __name__ == '__main__':
    main()
