import sys
import heapq


def main():
    N = int(sys.stdin.readline())
    small, large = [], []
    sCnt, lCnt = 0, 0
    for i in range(N):
        num = int(sys.stdin.readline())
        if sCnt == lCnt == 0:
            sCnt += 1
            heapq.heappush(small, -num)
        elif sCnt == 1 and lCnt == 0:
            smallV = -small[0]
            if smallV <= num:
                heapq.heappush(large, num)
            else:
                heapq.heappush(large, smallV)
                heapq.heappop(small)
                heapq.heappush(small, -num)
            lCnt += 1
        elif sCnt == lCnt: #좌우 같은상태에서 입력
            smallV, largeV = -small[0], large[0]
            if num <= smallV:
                sCnt += 1
                heapq.heappush(small, -num)
            else:
                if largeV < num:
                    heapq.heappush(small, -largeV)
                    heapq.heappop(large)
                    heapq.heappush(large, num)
                else:
                    heapq.heappush(small, -num)
                sCnt += 1
        else:
            smallV, largeV = -small[0], large[0]
            if smallV <= num:
                heapq.heappush(large, num)
            else:
                heapq.heappush(large, smallV)
                heapq.heappop(small)
                heapq.heappush(small, -num)
            lCnt += 1
        print(-small[0])


if __name__ == '__main__':
    main()
