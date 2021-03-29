import sys
from itertools import combinations


def main():
    global N, L, R, X, level
    N, L, R, X = map(int, sys.stdin.readline().split())
    level = sorted(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    for i in range(2, N + 1):
        cnt += choice(i)
    print(cnt)


def choice(num): # num개 고름
    global N, L, R, X, level
    cases = combinations(level, num)
    result = 0
    for case in cases:
        if L <= sum(case) <= R and case[num - 1] - case[0] >= X:
            result += 1
    return result


if __name__ == '__main__':
    main()
