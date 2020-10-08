def main():
    N, M = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    idx = [0] * M
    while True:
        for j in range(M):
            print(num[idx[j]], end = ' ')
        if num[idx[0]] == num[N - 1]:
            break
        print()
        idx[M - 1] += 1
        for j in range(M - 1, 0, -1):
            if idx[j] == N:
                idx[j - 1] += 1
                idx = idx[:j] + [idx[j - 1]] * (N - j)


if __name__ == "__main__":
    main()
