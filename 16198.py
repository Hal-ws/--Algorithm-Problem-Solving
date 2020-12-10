from itertools import permutations


def main():
    N = int(input())
    weights = list(map(int, input().split()))
    cases = [(i + 1) for i in range(N - 2)]
    cases = list(permutations(cases, N - 2))
    maxVal = 0
    for case in cases:
        tmp = getenergy(case, weights, N - 2)
        if maxVal < tmp:
            maxVal = tmp
    print(maxVal)


def getenergy(case, weights, l):
    energy = 0
    deletedchk = [1] * (l + 2)
    for i in range(l):
        idx = case[i]
        energy += (getleft(idx, deletedchk, weights) * getright(idx, deletedchk, weights, l + 2))
        deletedchk[idx] = 0
    return energy


def getleft(idx, deletedchk, weights):
    for i in range(idx -1, -1, -1):
        if weights[i] != 0 and deletedchk[i]:
            return weights[i]


def getright(idx, deletedchk, weights, N):
    for i in range(idx + 1, N):
        if weights[i] != 0 and deletedchk[i]:
            return weights[i]


if __name__ == "__main__":
    main()
