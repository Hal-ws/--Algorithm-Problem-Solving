def main():
    N = input()
    lN = len(N) ## N의 자리수
    N = int(N)
    ans = [0] * 10
    for i in range(10):
        ans[i] = getdigit(N, i, lN) #33
    for i in range(10):
        print(ans[i], end=' ')


def getdigit(N, num, lN): ## 각 자리수마다의 num(0~9)의 합을 구함
    ans = 0
    Ns = str(N)
    for i in range(1, lN + 1): ## i: i번째 자리에 오는걸 구함
        if i == 1:
            if num == 0:
                ans += N // 10
            elif int(Ns[lN - i]) >= num:
                ans += N // pow(10, i) + 1
            else:
                ans += N // pow(10, i)
        elif i == lN:
            if int(Ns[lN - i]) == num and num != 0:
                ans += N - num * pow(10, lN - 1) + 1
            if int(Ns[lN - i]) > num and num != 0:
                ans += pow(10, lN - 1)
        else:
            if int(Ns[lN - i]) >= num and num != 0:
                ans += (N // pow(10, i) + 1) * (N % pow(10, i) + 1)
            if int(Ns[lN - i]) < num and num != 0:
                ans += (N // pow(10, i)) * 10
            if num == 0:
                ans += (N // pow(10, i)) * 10
    return ans


if __name__ == "__main__":
    main()
