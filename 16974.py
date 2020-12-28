def main():
    N, X = map(int, input().split())
    ans = 0
    patty = [1] * 51
    layer = [1] * 51
    for i in range(1, 51):
        patty[i] = patty[i - 1] * 2 + 1
        layer[i] = layer[i - 1] * 2 + 3
    while X > 0:
        mid = layer[N] // 2 + 1
        if N == 0:
            ans += 1
            break
        if X == mid:
            ans += (patty[N - 1] + 1)
            X -= (layer[N - 1] + 2)
        elif X > mid:
            ans += (patty[N - 1] + 1)
            X -= (layer[N - 1] + 2)
        else:
            X -= 1
        N -= 1
    print(ans)


if __name__ == '__main__':
    main()
