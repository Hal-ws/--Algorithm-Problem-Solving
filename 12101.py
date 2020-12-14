def main():
    n, k = map(int, input().split())
    dp = [[[] for j in range(3)] for i in range(11)]
    dp[0][2].append('1')
    dp[1][1].append('2')
    dp[1][2].append('1+1')
    dp[2][0].append('3')
    for i in range(2, 11):
        for j in range(0, 3):
            if dp[i][j] == []: #
                dp[i][j] = getpoint(dp, i, j)
    ans = sorted(dp[n - 1][0] + dp[n - 1][1] + dp[n - 1][2])
    l = len(ans)
    if l >= k:
        print(ans[k - 1])
    else:
        print(-1)


def getpoint(dp, y, x):
    if x == 2: #최대값이 1기준
        return [dp[y - 1][x][0] + '+1']
    if x == 1: #최대값이 2
        result = []
        target = dp[y - 1][1]
        lt = len(target)
        for i in range(lt):
            result.append(target[i] + '+1')
        for j in range(1, 3):
            target = dp[y - 2][j]
            lt = len(target)
            for i in range(lt):
                result.append(target[i] + '+2')
        return result
    if x == 0: #최대값이 3
        result = []
        target = dp[y - 1][0]
        lt = len(target)
        for i in range(lt):
            result.append(target[i] + '+1')
        target = dp[y - 2][0]
        lt = len(target)
        for i in range(lt):
            result.append(target[i] + '+2')
        for j in range(3):
            target = dp[y - 3][j]
            if target != []:
                lt = len(target)
                for i in range(lt):
                    result.append(target[i] + '+3')
        return result


if __name__ == '__main__':
    main()
