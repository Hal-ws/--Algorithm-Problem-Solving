import sys


def main():
    N, M, H = map(int, sys.stdin.readline().split())
    students = [[]]
    for i in range(N):
        students.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0 for j in range(H + 1)] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(H + 1):
            dp[i][j] = dp[i - 1][j]
        for num in students[i]:
            for j in range(H + 1):
                if dp[i - 1][j] > 0 and j + num <= H:
                    dp[i][j + num] += dp[i - 1][j]
    print(dp[N][H] % 10007)


if __name__ == "__main__":
    main()
