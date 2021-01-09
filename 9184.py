import sys


def main():
    global dp
    dp = [[[0 for k in range(21)] for j in range(21)] for i in range(21)]
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                w(i, j, k)
    while 1:
        a, b, c = map(int, sys.stdin.readline().split())
        if a == b == c == -1:
            break
        elif a <= 0 or b <= 0 or c <= 0:
            ans = 1
        elif a > 20 or b > 20 or c > 20:
            ans = dp[20][20][20]
        else:
            ans = dp[a][b][c]
        print('w(%s, %s, %s) = %s' %(a, b, c, ans))


def w(a, b, c):
    global dp
    if dp[a][b][c] != 0:
        return
    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
        return 1
    elif a < b < c:
        v1, v2 ,v3 = dp[a][b][c - 1], dp[a][b - 1][c - 1], dp[a][b - 1][c]
        if v1 == 0:
            v1 = w(a, b, c - 1)
            dp[a][b][c - 1] = v1
        if v2 == 0:
            v2 = w(a, b - 1, c - 1)
            dp[a][b - 1][c - 1] = v2
        if v3 == 0:
            v3 = w(a, b - 1, c)
            dp[a][b - 1][c] = v3
        dp[a][b][c] = v1 + v2 - v3
        return dp[a][b][c]
    else:
        v1, v2, v3, v4 = dp[a - 1][b][c], dp[a - 1][b - 1][c], dp[a - 1][b][c - 1], dp[a - 1][b - 1][c - 1]
        if v1 == 0:
            v1 = w(a - 1, b, c)
            dp[a - 1][b][c] = v1
        if v2 == 0:
            v2 = w(a - 1, b - 1, c)
            dp[a - 1][b - 1][c] = v2
        if v3 == 0:
            v3 = w(a - 1, b, c - 1)
            dp[a - 1][b][c - 1] = v3
        if v4 == 0:
            v4 = w(a - 1, b - 1, c - 1)
            dp[a - 1][b - 1][c - 1] = v3
        dp[a][b][c] = v1 + v2 + v3 - v4
        return dp[a][b][c]


if __name__ == '__main__':
    main()
