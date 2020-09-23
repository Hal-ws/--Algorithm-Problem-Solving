import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    a = []
    for i in range(N):
        a.append(list(map(int, sys.stdin.readline().split())))
    K = int(sys.stdin.readline())
    for ii in range(K):
        i, j, x, y = map(int, sys.stdin.readline().split())
        ans = 0
        for iii in range(i - 1, x):
            ans += sum(a[iii][j - 1:y])
        print(ans)


if __name__ == "__main__":
    main()
