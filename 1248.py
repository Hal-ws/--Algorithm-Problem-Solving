import sys


def main():
    global N, matrix, ansFlag
    N = int(sys.stdin.readline())
    mark = list(sys.stdin.readline()[:N * (N + 1) // 2])
    matrix = [[0 for j in range(N)] for i in range(N)]
    ansFlag = 0
    k = 0
    for i in range(N):
        for j in range(i, N):
            matrix[i][j] = mark[k]
            k += 1
    if matrix[0][0] == '0':
        dfs([0], 1) #
    elif matrix[0][0] == '+':
        for i in range(1, 11):
            dfs([i], 1)
    else:
        for i in range(-1, -11, -1):
            dfs([i], 1)


def dfs(nList, cnt): # 현재 저장된 nList, 현재까지 적은 숫자의 수
    global N, matrix, ansFlag
    if ansFlag:
        return
    if cnt == N:
        ansFlag = 1
        for i in range(N):
            print(nList[i], end=' ')
        return
    nxtNums = [1] * 21
    for i in range(cnt + 1):
        sumV = sum(nList[i:])
        if matrix[i][cnt] == '+': # 다음 숫자까지의 합이 +가 돼야함
            if sumV < 0:
                if sumV <= -10:
                    return
                for j in range(10 - sumV + 1):
                    nxtNums[j] = 0
            elif sumV == 0:
                for j in range(11):
                    nxtNums[j] = 0
            else:
                for j in range(10 - sumV + 1):
                    nxtNums[j] = 0
        elif matrix[i][cnt] == '0': # 다음 숫자까지의 합이 0이 돼야함
            if sumV < -10 or sumV > 10:
                return
            nxtNums = [0] * 21
            nxtNums[-sumV + 10] = 1
        else: #다음 숫자까지의 합이 음수가 돼야함
            if sumV > 0:
                if sumV >= 10:
                    return
                for j in range(10 - sumV, 21):
                    nxtNums[j] = 0
            elif sumV == 0:
                for j in range(10, 21):
                    nxtNums[j] = 0
            else:
                for j in range(10 - sumV, 21):
                    nxtNums[j] = 0
    for i in range(21):
        if nxtNums[i]:
            nList.append(i - 10)
            dfs(nList, cnt + 1)
            nList.pop()


if __name__ == '__main__':
    main()
