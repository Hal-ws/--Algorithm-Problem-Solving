import sys
from math import sqrt
from itertools import combinations


def main():
    global vectors, pIdx, points, ans, N
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        ans = pow(10, 8)
        pIdx = [i for i in range(N)]
        points = []
        for i in range(N):
            points.append(list(map(int, sys.stdin.readline().split())))
        cases = combinations(pIdx, N // 2) # 10
        for case in cases:
            minusChk = [0 for i in range(N)]
            vec = [0, 0]  # x, y 저장
            for i in range(N // 2):
                minusChk[case[i]] = 1
            for i in range(N):
                idx = pIdx[i]
                x, y = points[idx][0], points[idx][1]
                if minusChk[idx]:
                    vec[0] += x
                    vec[1] += y
                else:
                    vec[0] -= x
                    vec[1] -= y
            tmpAns = sqrt(pow(vec[0], 2) + pow(vec[1], 2))
            if tmpAns < ans:
                ans = tmpAns
        print(ans)


if __name__ == '__main__':
    main()
