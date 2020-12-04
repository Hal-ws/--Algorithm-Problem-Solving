import sys
from _collections import deque


def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().split())
        buildTime = [0] + list(map(int, sys.stdin.readline().split()))
        bconnect = [[] for i in range(N + 1)] # i번 빌딩을 짓기 전에 지어야 하는 건물 저장
        aconnect = [[] for i in range(N + 1)] # i번 빌딩을 짓고 지을 수 있는 빌딩
        builded = [0] * (N + 1) # 이미 지어진 건물들의 건설시간 표시
        time = 0
        for i in range(K):
            before, after = map(int, sys.stdin.readline().split())
            bconnect[after].append(before)
            aconnect[before].append(after)
        print('bconnect: %s' %bconnect)
        target = int(sys.stdin.readline())  # 지어야하는 건물 number
        nessesary = getnessesary(set(), bconnect, target)
        ln = len(nessesary)
        q = deque()
        for i in range(ln):
            q.append(nessesary[i])
        q.append(target)
        while len(q) > 0:
            buildChk(q, bconnect, buildTime, builded)
            print(q)
        print(builded)


def getnessesary(nessesary, bconnect, target):
    q = deque()
    q.append(target)
    while len(q) > 0:
        l = len(bconnect[q[0]])
        for i in range(l):
            nessesary.add(bconnect[q[0]][i])
            q.append(bconnect[q[0]][i])
        q.popleft()
    return list(nessesary)


def buildChk(q, bconnect, buildTime, builded): #q[0]에 있는 건물을 지을 수 있는지 확인한다.
    cur = q[0] #지금 지으려고 하는 빌딩
    time = 0
    flag = 1 #지을 수 없으면 flag가 0임
    l = len(bconnect[cur])
    if l == 0: # 선행 빌딩 필요없음. 건설 가능함
        time += buildTime[cur]
        builded[cur] = buildTime[cur]
        q.popleft()
        return
    for i in range(l):
        if builded[bconnect[cur][i]] == 0: #선행 건물중 안지어진게 있음
            q.append(bconnect[cur][i])
            flag = 0
        tmpTime = buildTime[bconnect[cur][i]]
        if time < tmpTime:
            time = tmpTime
    if flag: #지금 건물 지음
        builded[cur] = time + buildTime[cur] # 지금 건물을 지은데 걸린 시간 입력(제일 오래 걸리는 시간 + cur 짓는데 걸린시간)
        q.popleft()


if __name__ == "__main__":
    main()
