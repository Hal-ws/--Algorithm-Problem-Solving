import sys
from itertools import permutations


def main():
    N = int(sys.stdin.readline())
    hitterresult = []
    for i in range(N):
        hitterresult.append([0] + list(map(int, sys.stdin.readline().split())))
    lineup = [2, 3, 4, 5, 6, 7, 8, 9]
    cases = list(permutations(lineup))
    lc = len(cases)
    for i in range(lc):
        cases[i] = list(cases[i])
        cases[i].insert(3, 1)
    ans = 0
    for i in range(lc):
        temp = getans(cases[i], hitterresult, N)
        if temp >= ans:
            ans = temp
    print(ans)


def getans(case, hitterresult, N):
    inning = 0
    order = 0 ## 타순: case[0]~case[8] 0번타순~8번타순의 선수들이 해당 이닝에 내는 점수
    score = 0
    while inning < N:
        outcnt = 0
        base = [0, 0, 0]  ## 1루, 2루, 3루
        while outcnt < 3:
            if hitterresult[inning][case[order]] == 0:
                outcnt += 1
            elif hitterresult[inning][case[order]] == 1:
                score += base[2]
                base[1], base[2] = base[0], base[1]
                base[0] = 1
            elif hitterresult[inning][case[order]] == 2:
                score += (base[2] + base[1])
                base[2] = base[0]
                base[1] = 1
                base[0] = 0
            elif hitterresult[inning][case[order]] == 3:
                score += base[0] + base[1] + base[2]
                base[2] = 1
                base[0], base[1] = 0, 0
            elif hitterresult[inning][case[order]] == 4:
                score += base[0] + base[1] + base[2] + 1
                base[0], base[1], base[2] = 0, 0, 0
            order += 1
            if order == 9:
                order = 0
        inning += 1
    return score


if __name__ == "__main__":
    main()
