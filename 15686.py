import sys
from itertools import combinations


def main():
    N, M = map(int, sys.stdin.readline().split())
    city = []
    chickenPos, housePos = [], []
    for i in range(N):
        city.append(list(map(int, sys.stdin.readline().split())))
        for j in range(N):
            if city[i][j] == 2:
                chickenPos.append([i, j])
            if city[i][j] == 1:
                housePos.append([i, j])
    cases = list(combinations(chickenPos, M))
    lc = len(cases)
    ans = -1
    for i in range(lc):
        temp = getchikendis(housePos, cases[i])
        if ans == - 1 or temp <= ans:
            ans = temp
    print(ans)


def getchikendis(housePos, case):
    lh, lc = len(housePos), len(case)
    cityChickenDis = 0
    for i in range(lh):
        chickenDis = -1
        for j in range(lc):
            distance = abs(case[j][0] - housePos[i][0]) + abs(case[j][1] - housePos[i][1])
            if distance <= chickenDis or chickenDis == -1:
                chickenDis = distance
        cityChickenDis += chickenDis
    return cityChickenDis


if __name__ == "__main__":
    main()
