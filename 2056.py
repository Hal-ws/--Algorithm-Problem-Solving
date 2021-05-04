import sys
from _collections import deque


def main():
    N = int(sys.stdin.readline())
    pWork = [0] * N # i번 작업 이전에 해야하는 선행 작업
    connect = [[] for i in range(N)]
    workTime = [0] * N # i번 작업을 하는데 걸리는 시간
    startTime = [0] * N # i번 작업을 시작하는 시간
    endTime = [0] * N # i번 작업을 종료하는 시간
    q = deque()
    for i in range(N):
        inputList = list(map(int, sys.stdin.readline().split()))
        workTime[i] = inputList[0]
        if inputList[1] == 0:
            q.append(i) # i번 작업 큐에 추가
        else:
            for j in range(2, len(inputList)):
                pWork[i] += 1
                connect[inputList[j] - 1].append(i)
    while len(q) > 0:
        wIdx = q.popleft()
        endTime[wIdx] = startTime[wIdx] + workTime[wIdx]
        for nxt in connect[wIdx]:
            pWork[nxt] -= 1
            if startTime[nxt] <= endTime[wIdx]:
                startTime[nxt] = endTime[wIdx]
            if pWork[nxt] == 0:
                q.append(nxt)
    print(max(endTime))


if __name__ == '__main__':
    main()
