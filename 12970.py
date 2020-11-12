def main():
    N, K = map(int, input().split())
    Acnt = N // 2
    Bcnt = N - Acnt
    BIdx, AIdx = Bcnt - 1, N - 1
    if K > Acnt * Bcnt:
        print(-1)
    else:
        ans = list("B" * Bcnt + "A" * Acnt)
        cnt = 0
        while cnt < K:
            if K - cnt >= Acnt:
                ans[AIdx], ans[BIdx] = ans[BIdx], ans[AIdx]
                AIdx -= 1
                BIdx -= 1
                cnt += Acnt
            else:
                ans[BIdx], ans[BIdx + K - cnt] = ans[BIdx + K - cnt], ans[BIdx]
                cnt += K - cnt
        for i in range(N):
            print(ans[i], end='')


if __name__ == "__main__":
    main()
