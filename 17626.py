def main():
    N = int(input())
    for i in range(N):
        if i * i <= N:
            maxVal = i
        else:
            break
    dp = [[0 for j in range(N + 1)] for i in range(5)]
    for j in range(1, maxVal + 1):
        dp[1][j * j] = 1
        if j * j == N:
            print(1)
            return
    for i in range(2, 5): # 사용 숫자 갯수 i - 1인거랑 비교
        for j in range(N + 1):
            if dp[i - 1][j]: # 사용갯수가 i - 1개인것 중 값이 j인게 존재할때
                for k in range(1, maxVal + 1):
                    if j + k * k <= N:
                        dp[i][j + k * k] = 1
                        if j + k * k == N:
                            print(i)
                            return


if __name__ == '__main__':
    main()
