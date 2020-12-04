import sys


def main():
    N = int(sys.stdin.readline())
    table = []
    for i in range(N):
        table.append(list(map(int, sys.stdin.readline().split())))
    dp = [0] * N
    ans = 0
    for i in range(N):
        jump = table[i][0] - 1 # 끝나는 날짜가 얼마 후인지 저장
        if i + jump < N:
            if i > 0:
                dp[i + jump] = max(max(dp[i + jump], table[i][1] + dp[i - 1]), dp[i + jump - 1])
            else:
                dp[i + jump] = max(max(dp[i + jump], table[i][1]), dp[i + jump - 1])
        if i > 0:
            dp[i] = max(dp[i - 1], dp[i])
        if dp[i] >= ans:
            ans = dp[i]
    print(ans)


if __name__ == "__main__":
    main()
