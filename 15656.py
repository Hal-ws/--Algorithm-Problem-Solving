def main():
    N, M = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    idx = [0] * M
    last = pow(N, M)
    for i in range(last):
        for j in range(M):
            print(num[idx[j]], end = ' ')
        print()
        idx[M - 1] += 1
        for j in range(M - 1, 0, -1):
            if idx[j] == N:
                idx[j] = 0
                idx[j - 1] += 1


if __name__ == "__main__":
    main()
