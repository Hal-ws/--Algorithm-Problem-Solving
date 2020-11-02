def main():
    N, M = map(int, input().split())
    square = [[0] * (M + 1) + [0]]
    for i in range(N):
        square.append([0] + list(map(int, input().split())) + [0])
    square.append([0] * (M + 2))
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if square[i][j] != 0:
                ans += 2
                if square[i - 1][j] <= square[i][j]:
                    ans += (square[i][j] - square[i - 1][j])
                if square[i + 1][j] <= square[i][j]:
                    ans += (square[i][j] - square[i + 1][j])
                if square[i][j - 1] <= square[i][j]:
                    ans += (square[i][j] - square[i][j - 1])
                if square[i][j + 1] <= square[i][j]:
                    ans += (square[i][j] - square[i][j + 1])
    print(ans)


if __name__ == "__main__":
    main()
