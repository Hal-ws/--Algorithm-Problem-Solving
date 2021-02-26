import sys


def main():
    global T, l, numList
    T = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    l1 = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    l2 = list(map(int, sys.stdin.readline().split()))
    matrix1 = [[0 for j in range(n)] for i in range(n)]
    matrix2 = [[0 for j in range(m)] for i in range(m)]
    ans = 0
    for i in range(n):
        matrix1[i][i] = l1[i]
    for i in range(n):
        for j in range(i + 1, n):
            matrix1[i][j] = matrix1[i][j - 1] + l1[j]
    for i in range(m):
        matrix2[i][i] = l2[i]
    for i in range(m):
        for j in range(i + 1, m):
            matrix2[i][j] = matrix2[i][j - 1] + l2[j]
    numList = []
    for i in range(m):
        for j in range(i, m):
            numList.append(matrix2[i][j])
    numList.sort()
    ansDic = {}
    l = len(numList)
    for i in range(n):
        for j in range(i, n):
            tmp = matrix1[i][j]
            if ansDic.get(tmp) == None:
                tmpAns = getans(matrix1[i][j])
                ansDic[tmp] = tmpAns
                ans += tmpAns
            else:
                ans += ansDic[tmp]
    print(ans)


def getans(std):
    global T, l, numList
    lower, upper = -1, -1
    start, end = 0, l - 1
    target = T - std
    while start <= end:
        mid = (start + end) // 2
        if numList[mid] >= target:
            if numList[mid] == target:
                lower = mid
            end = mid - 1
        if numList[mid] < target:
            start = mid + 1
    start, end = 0, l - 1
    while start <= end:
        mid = (start + end) // 2
        if numList[mid] <= target:
            if numList[mid] == target:
                upper = mid
            start = mid + 1
        if numList[mid] > target:
            end = mid - 1
    if lower == upper == -1:
        return 0
    return upper - lower + 1


if __name__ == '__main__':
    main()
