def main():
    N = int(input())
    dp = [[0 for j in range(11)] for i in range(11)]
    for j in range(1, 11):
        dp[1][j] = 1
    for i in range(2, 11):
        for j in range(1, 11):
            tmp = 0
            for k in range(j):
                tmp += dp[i - 1][k]
            dp[i][j] = tmp
    culCnt = -1 # 누적
    flag = 0
    ans = ''
    for i in range(1, 11):
        for j in range(11):
            culCnt += dp[i][j]
            if culCnt >= N: # 시작 자릿수와 수 찾음
                flag = 1
                level, num = i, j - 1 # 자릿수, 수
                ans += str(j - 1)
                N = N - culCnt + dp[i][j] # 0부터 세므로 1을 더해준다
                break
        if flag:
            break
    if flag == 0:
        print(-1)
    else:
        while level > 1:
            level -= 1
            tmpSum = 0
            for j in range(11):
                if j == 0:
                    num = j
                else:
                    num = j - 1
                tmpSum += dp[level][j]
                if tmpSum >= N:
                    ans += str(num)
                    N = N - tmpSum + dp[level][j]
                    break
        print(ans)


if __name__ == '__main__':
    main()
