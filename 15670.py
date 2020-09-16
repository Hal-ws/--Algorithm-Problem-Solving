import sys
from copy import deepcopy

def main():
    N, M = map(int, sys.stdin.readline().split())
    road = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        todayRoad = deepcopy(road)
        start, end = map(int, sys.stdin.readline().split())
        temp = todayRoad[start - 1:end]
        temp.reverse()
        todayRoad = todayRoad[:start - 1] + temp + todayRoad[end:]
        print(countuplen(N, todayRoad))


def countuplen(N, todayRoad):
    cnt, start = 0, 0
    if N < 2:
        return 1
    while start < N - 1:
        cnt += 1
        for i in range(start + 1, N):
            if todayRoad[i] < todayRoad[i - 1]:
                break
        start = i
    if todayRoad[N - 1] < todayRoad[N - 2]:
        cnt += 1
    return cnt

if __name__ == "__main__":
    main()
