import sys


def main():
    N = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    while 1:
        for i in range(N):
            if B[i] % 2 != 0:
                B[i] -= 1
                cnt += 1
        if sum(B) == 0:
            ans = cnt
            break
        for i in range(N):
            B[i] = B[i] // 2
        cnt += 1
    print(ans)


if __name__ == '__main__':
    main()
