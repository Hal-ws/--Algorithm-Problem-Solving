import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    road = list(map(int, sys.stdin.readline().split()))
    sCnt = getCntList(road)
    road.reverse()
    rCnt = getCntList(road)
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        start, end = start - 1, end - 1
        if start == end:
            print(sCnt[N - 1])
        else:
            rStart, rEnd = N - end - 1, N - start - 1 #
            cnt = rCnt[rEnd] - rCnt[rStart] + 1
            if start != 0:
                cnt += sCnt[start - 1]
                if road[start - 1] > road[end]:
                    cnt += 1
            if end != N - 1:
                cnt += (sCnt[N - 1] - sCnt[end + 1] + 1)
                if road[end + 1] < road[start]:
                    cnt += 1
            print(cnt)


def getCntList(road):
    l = len(road)
    cntList = [0 for i in range(l)]
    cntList[0] = 1
    for i in range(1, l):
        if road[i - 1] < road[i]:
            cntList[i] = cntList[i - 1]
        else:
            cntList[i] = cntList[i - 1] + 1
    return cntList


if __name__ == "__main__":
    main()
