def main():
    a = input()
    l = len(a)
    cnt = [0, 0, 0] # A, B, C의 갯수
    for p in a:
        cnt[ord(p) - 65] += 1
    dp = [[[[] for i in range(l + 1)] for j in range(l + 1)] for k in range(l + 1)]
    for i in range(cnt[0] + 1):
        for j in range(cnt[1] + 1):
            for k in range(cnt[2] + 1):
                if i == 1 and j == 0 and k == 0:
                    dp[i][j][k].append('A')
                elif i == 0 and j == 1 and k == 0:
                    dp[i][j][k].append('B')
                elif i == 0 and j == 0 and k == 1:
                    dp[i][j][k].append('C')
                elif i > 0 or j > 0 or k > 0:
                    l = i + j + k
                    if i >= 1:
                        tmp = dp[i - 1][j][k] # A를 추가해줄것
                        if tmp != []: #불가능한 경우가 아니면
                            for word in tmp:
                                dp[i][j][k].append(word + 'A')
                    if j >= 1:
                        tmp = dp[i][j - 1][k] # B를 추가
                        if tmp != []:
                            for word in tmp:
                                if word[l - 2] != 'B':
                                    dp[i][j][k].append(word + 'B')
                    if k >= 1:
                        tmp = dp[i][j][k - 1] # C를 추가
                        if tmp != []:
                            for word in tmp:
                                if l == 2:
                                    if word[l - 2] != 'C':
                                        dp[i][j][k].append(word + 'C')
                                if l > 2:
                                    if word[l - 2] != 'C' and word[l - 3] != 'C':
                                        dp[i][j][k].append(word + 'C')
    ans = dp[cnt[0]][cnt[1]][cnt[2]]
    if ans == []:
        print(-1)
    else:
        print(ans[0])


if __name__ == '__main__':
    main()
