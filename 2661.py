def main():
    global N, ansFlag, ans
    N = int(input())
    numList = [1]
    ansFlag = 0
    dfs(numList, 1)
    for i in range(N):
        print(ans[i], end='')


def dfs(numList, l):
    global N, ansFlag, ans
    if l == N and ansFlag == 0:
        ansFlag = 1
        ans = [numList[i] for i in range(N)]
        return
    if ansFlag:
        return
    for n in range(1, 4):
        if chkPoss(numList, n):
            numList.append(n)
            dfs(numList, l + 1)
            numList.pop()
    return


def chkPoss(numList, n):
    l = len(numList) + 1
    numList.append(n)
    for i in range(1, l // 2 + 1):
        if numList[l - i:] == numList[l - 2 * i:l - i]:
            numList.pop()
            return 0
    numList.pop()
    return 1


if __name__ == '__main__':
    main()
