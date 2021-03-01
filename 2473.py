import sys


def main():
    N = int(sys.stdin.readline())
    numList = list(map(int, sys.stdin.readline().split()))
    numList.sort()
    minVal = 3000000001
    ans = [None, None, None]
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            s, e = j + 1, N - 1
            while s <= e:
                mid = (s + e) // 2
                tmpVal = numList[i] + numList[j] + numList[mid]
                if abs(tmpVal) < minVal:
                    minVal = abs(tmpVal)
                    ans[0], ans[1], ans[2] = numList[i], numList[j], numList[mid]
                if tmpVal == 0:
                    for k in range(3):
                        print(ans[k], end=' ')
                    return
                if tmpVal > 0:
                    e = mid - 1
                if tmpVal < 0:
                    s = mid + 1
    for i in range(3):
        print(ans[i], end=' ')


if __name__ == '__main__':
    main()
