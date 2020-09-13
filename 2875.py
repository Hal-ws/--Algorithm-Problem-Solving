def main():
    N, M, K = map(int, input().split())
    maxteam = min(N // 2, M)
    leftmember = N + M - (maxteam * 3)
    if leftmember >= K:
        print(maxteam)
    else:
        discnt = -leftmember + K
        if discnt % 3 == 0:
            print(maxteam - discnt // 3)
        else:
            print(maxteam - discnt // 3 - 1)


if __name__ == "__main__":
    main()
