def main():
    N = int(input())
    ans = [[0, 1, 0], [1, 1, 1]]
    if N <= 2:
        print(sum(ans[N - 1]))
    else:
        for i in range(2, N):
            val1 = sum(ans[i - 2])
            val2 = sum(ans[i - 1])
            ans.append([val1, val2, val1])
        print(sum(ans[N - 1]) % 10007)


if __name__ == "__main__":
    main()
