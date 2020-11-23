def main():
    N, M = map(int, input().split())
    if N >= 3:
        if M <= 4:
            ans = M
        elif M < 7:
            ans = 4
        else:
            ans = 5 + (M - 7)
    if N == 1:
        ans = 1
    if N == 2:
        if M < 3:
            ans = 1
        elif M < 5:
            ans = 2
        elif M < 7:
            ans = 3
        else:
            ans = 4
    print(ans)


if __name__ == "__main__":
    main()
