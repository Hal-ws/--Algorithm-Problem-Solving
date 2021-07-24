import sys
from collections import deque


def main():
    maxCnt = int(sys.stdin.readline())
    scores = [0 for i in range(maxCnt + 1)]
    relations = [[] for i in range(maxCnt + 1)]
    candidates = []
    ansCnt = 0
    minScore = 51
    while 1:
        a, b = map(int, sys.stdin.readline().split())
        if a == b == -1:
            break
        relations[a].append(b)
        relations[b].append(a)
    for i in range(1, maxCnt + 1):
        scores[i] = getscore(i, relations, maxCnt)
    for i in range(1, maxCnt + 1):
        if scores[i] < minScore:
            minScore = scores[i]
    for i in range(1, maxCnt + 1):
        if scores[i] == minScore:
            candidates.append(i)
            ansCnt += 1
    print('%s %s' %(minScore, ansCnt))
    for i in range(len(candidates)):
        print(candidates[i], end=' ')


def getscore(p, relations, maxCnt):
    maxDis = 0
    q = deque()
    q.append([p, 0])
    visit = [0 for i in range(maxCnt + 1)]
    visit[p] = 1
    while len(q) > 0:
        tmp = q.popleft()
        cur, dis = tmp[0], tmp[1]
        if dis > maxDis:
            maxDis = dis
        for nxtP in relations[cur]:
            if visit[nxtP] == 0:
                visit[nxtP] = 1
                q.append([nxtP, dis + 1])
    return maxDis


if __name__ == "__main__":
    main()
