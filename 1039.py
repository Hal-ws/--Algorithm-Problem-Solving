import sys
from collections import deque
from copy import deepcopy


def main():
    N, K = map(str, sys.stdin.readline().split())
    start = list(N)
    K = int(K)
    l = len(start)
    answer = -1
    for i in range(l):
        start[i] = int(start[i])
    visit = [[0 for j in range(1000001)] for i in range(11)]
    visit[0][int(N)] = 1
    q = deque()
    q.append([start, 0])
    while len(q) > 0:
        tmp = q.popleft()
        nList, cnt = tmp[0], tmp[1]
        val = getVal(tmp[0], l)
        if cnt == K:
            if val > answer:
                answer = val
        else:
            for i in range(l - 1):
                for j in range(i + 1, l):
                    if i == 0 and nList[j] == 0: # 바뀐 수가 0이 될때
                        continue
                    else: # 바꾸는것 가능할 때
                        nxtList = deepcopy(nList)
                        nxtList[i], nxtList[j] = nxtList[j], nxtList[i] # 교체
                        nxtVal = getVal(nxtList, l)
                        if visit[cnt + 1][nxtVal] == 0:
                            visit[cnt + 1][nxtVal] = 1
                            q.append([nxtList, cnt + 1])
    print(answer)


def getVal(nList, l):
    result = 0
    for i in range(l - 1, -1, -1):
        result += nList[i] * pow(10, l - 1 - i)
    return result


if __name__ == '__main__':
    main()
