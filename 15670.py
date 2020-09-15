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
        print('todayRoad: %s' %todayRoad)
        print(countuplen(N, todayRoad))


def countuplen(N, todayRoad):
    cnt, start, end = 0, 0, 0
    if N < 2:
        return 1
    while end < N:
        cnt += 1
        end = start + 1
        print('start: %s end: %s' % (start, end))
        for i in range(end, N):
            print('i: %s' %i)
            if todayRoad[i] < todayRoad[i - 1]:
                start = i
                break
    return cnt

if __name__ == "__main__":
    main()
