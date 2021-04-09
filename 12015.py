import sys


def main():
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    LIS = [nList[0]]
    for i in range(1, N):
        num = nList[i]
        if LIS[-1] < num:
            LIS.append(num)
        else:
            left, right = 0, len(LIS) - 1
            while left <= right:
                mid = (left + right) // 2
                if LIS[mid] < num:
                    left = mid + 1
                else:
                    right = mid
                    if left == right:
                        mid = right
                        break
            LIS[mid] = num
    print(len(LIS))


if __name__ == '__main__':
    main()
