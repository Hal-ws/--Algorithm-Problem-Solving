import sys


def main():
    N = int(sys.stdin.readline())
    nList = []
    if N == 1:
        print(1)
        return
    for i in range(N):
        nList.append(int(sys.stdin.readline()))
    nList.sort()
    left, right = 2, N
    answer = 2
    while left <= right:
        mid = (left + right) // 2
        if getLen(nList, mid, N): # 길이 l인 등차수열 생성가능
            left = mid + 1
        else:
            right = mid - 1
    print(answer)


def getLen(nList, l, N):

    return 0


if __name__ == '__main__':
    main()
