import sys
import heapq


def main():
    N = int(sys.stdin.readline())
    q = []
    cnt = 0
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            heapq.heappush(q, tmp[j])
            cnt += 1
            if N < cnt:
                heapq.heappop(q)
                cnt -= 1
    ans = heapq.heappop(q)
    print(ans)


if __name__ == '__main__':
    main()
