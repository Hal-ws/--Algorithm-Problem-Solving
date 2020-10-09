import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    sumList = [0] * (N + 1)
    sumList[1] = num[0]
    for i in range(2, N + 1):
        sumList[i] = num[i - 1] + sumList[i - 1]
    for i in range(M):
        start, end = map(int, sys.stdin.readline().split())
        print(sumList[end] - sumList[start - 1])


if __name__ == "__main__":
    main()
