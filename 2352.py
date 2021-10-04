import sys
from bisect import bisect_left


def main():
    N = int(input())
    ports = list(map(int, sys.stdin.readline().split()))
    LIS = [ports[0]]
    for i in range(1, N):
        num = ports[i]
        if LIS[-1] < num:
            LIS.append(num)
        else:
            idx = bisect_left(LIS, num)
            LIS[idx] = num
    print(len(LIS))


if __name__ == "__main__":
    main()
