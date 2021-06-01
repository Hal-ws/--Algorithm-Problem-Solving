import sys
from bisect import bisect_left


def main():
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    LIS = [nList[0]]
    for i in range(1, N):
        num = nList[i]
        if num > LIS[-1]:
            LIS.append(num)
        else:
            idx = bisect_left(LIS, num)
            LIS[idx] = num
    print(len(LIS))


if __name__ == '__main__':
    main()
