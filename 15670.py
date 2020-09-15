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
    cnt = 0
    return cnt

if __name__ == "__main__":
    main()
