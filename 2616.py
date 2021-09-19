import sys


def main():
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    maxVal = int(sys.stdin.readline())
    sumList = [0] * N
    sumList[0] = nList[0]
    for i in range(1, N):
        sumList[i] = sumList[i - 1] + nList[i]
    first = [0] * N
    for i in range(maxVal - 1, N):
        if i == maxVal - 1:
            first[i] = sumList[i]
        else:
            first[i] = max(sumList[i] - sumList[i - maxVal], first[i - 1])
    second = [0] * N
    for i in range(maxVal * 2 - 1, N):
        second[i] = max(sumList[i] - sumList[i - maxVal] + first[i - maxVal], second[i - 1])
    third = [0] * N
    for i in range(maxVal * 3 - 1, N):
        third[i] = max(sumList[i] - sumList[i - maxVal] + second[i - maxVal], third[i - 1])
    print(third[N - 1])


if __name__ == "__main__":
    main()
