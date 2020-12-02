from math import gcd
import sys


def lcm(x, y):
    return x * y // gcd(x, y)


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        endYear = lcm(N, M)
        curY = 1 #현재 년도. 첫해에서 시작
        A = 0
        while 1:
            if curY > endYear:
                break
            if M >= N:
                curY = A * M + x
                B = (curY - y) / N
                if B % 1 == 0 and B >= 0:
                    break
            else:
                curY = A * N + y
                B = (curY - x) / M
                if B % 1 == 0 and B >= 0:
                    break
            A += 1
        if curY > endYear:
            print(-1)
        else:
            print(curY)


if __name__ == "__main__":
    main()
