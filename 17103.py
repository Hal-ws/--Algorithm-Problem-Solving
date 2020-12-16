import sys
from math import sqrt

def main():
    chk = [1] * 1000001
    chk[1] = 0
    maxCnt = int(sqrt(1000000))
    for i in range(2, maxCnt + 1):
        if chk[i]:
            for j in range(i * i, 1000001, i):
                chk[j] = 0
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        cnt = 0
        for j in range(2, N // 2 + 1):
            if chk[j] and chk[N - j]:
                cnt += 1
        print(cnt)


if __name__ == '__main__':
    main()
