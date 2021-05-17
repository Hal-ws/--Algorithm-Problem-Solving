import sys
import heapq


def main():
    N = int(sys.stdin.readline())
    timetable = []
    for _ in range(N):
        timetable.append(list(map(int, sys.stdin.readline().split())))
    timetable.sort()
    usingCom = []
    emptyCom = []
    cntList = []
    for pIdx in range(N):
        start, end = timetable[pIdx][0], timetable[pIdx][1]
        while len(usingCom) > 0: # emptyCom에 추가해줌
            tmp = heapq.heappop(usingCom)
            time, cIdx = tmp[0], tmp[1]
            if time < start:
                heapq.heappush(emptyCom, cIdx)
            else:
                heapq.heappush(usingCom, [time, cIdx])
                break
        if len(emptyCom) > 0:
            com = heapq.heappop(emptyCom)
            heapq.heappush(usingCom, [end, com])
            cntList[com] += 1
        else:
            cntList.append(1)
            heapq.heappush(usingCom, [end, len(cntList) - 1])
    print(len(cntList))
    for cnt in cntList:
        print(cnt, end=' ')


if __name__ == '__main__':
    main()
