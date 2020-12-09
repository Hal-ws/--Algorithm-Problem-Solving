import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    impossible = [[0 for i in range(201)] for j in range(201)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        impossible[a][b] = 1
        impossible[b][a] = 1
    ans = [0]
    for i in range(1, N - 1):
        dfs(impossible, i, None, None, N, ans)
    print(ans[0])


def dfs(impossible, first, second, third, N, ans):
    if second == None:
        for i in range(first + 1, N):
            dfs(impossible, first, i, None, N, ans)
    elif third == None:
        for i in range(second + 1, N + 1):
            dfs(impossible, first, second, i, N, ans)
    else:
        if impossible[first][second] != 1 and impossible[first][third] != 1 and impossible[second][third] != 1:
            ans[0] += 1


if __name__ == "__main__":
    main()
