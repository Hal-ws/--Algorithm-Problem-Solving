import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    pSum = [0 for i in range(N)] # 행 기준 합
    vSum = [0 for i in range(M)] # 열 기준 합
    for i in range(N):
        tmpSum = 0
        if i == 0 or i == N - 1:
            for j in range(M):
                if j == 0 or j == M - 1:
                    tmpSum += board[i][j]
                else:
                    tmpSum += board[i][j] * 2
        else:
            for j in range(M):
                if j == 0 or j == M - 1:
                    tmpSum += board[i][j] * 2
                else:
                    tmpSum += board[i][j] * 4
        pSum[i] = tmpSum
    for j in range(M):
        tmpSum = 0
        if j == 0 or j == M - 1:
            for i in range(N):
                if i == 0 or i == N - 1:
                    tmpSum += board[i][j]
                else:
                    tmpSum += board[i][j] * 2
        else:
            for i in range(N):
                if i == 0 or i == N - 1:
                    tmpSum += board[i][j] * 2
                else:
                    tmpSum += board[i][j] * 4
        vSum[j] = tmpSum
    ans = sum(pSum)
    for i in range(1, N - 1): # 0번과 i 번째 행을 교환
        tmp = 0
        for j in range(N):
            if j == 0:
                tmp += pSum[j] * 2
            elif j == i:
                tmp += pSum[j] // 2
            else:
                tmp += pSum[j]
        if ans < tmp:
            ans = tmp
    for i in range(1, N - 1): # N - 1번과 i번째 행을 교환
        tmp = 0
        for j in range(N):
            if j == N - 1:
                tmp += pSum[j] * 2
            elif j == i:
                tmp += pSum[j] // 2
            else:
                tmp += pSum[j]
        if ans < tmp:
            ans = tmp
    for i in range(1, M - 1): # 0번과 i번째 열을 교환
        tmp = 0
        for j in range(M):
            if j == 0:
                tmp += vSum[j] * 2
            elif j == i:
                tmp += vSum[j] // 2
            else:
                tmp += vSum[j]
        if ans < tmp:
            ans = tmp
    for i in range(1, M - 1):
        tmp = 0
        for j in range(M):
            if j == M - 1:
                tmp += vSum[j] * 2
            elif j == i:
                tmp += vSum[j] // 2
            else:
                tmp += vSum[j]
        if ans < tmp:
            ans = tmp
    print(ans)


if __name__ == '__main__':
    main()
