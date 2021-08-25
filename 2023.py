import sys
from math import sqrt


def main():
    N = int(sys.stdin.readline())
    nList = [2, 3, 5, 7]
    for i in range(4):
        dfs(nList[i], N, 1)


def dfs(num, N, l):
    if l == N: # 길이 만족
        print(num)
        return
    for addN in range(1, 10, 2):
        if chkPrime(num * 10 + addN):
            dfs(num * 10 + addN, N, l + 1)


def chkPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


if __name__ == "__main__":
    main()
