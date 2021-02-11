from itertools import combinations
import sys


def main():
    global table, total, N
    N, M = map(int, sys.stdin.readline().split())
    table = []
    total = [0] * 26
    essential = [1] * 26
    for i in range(N):
        word = sys.stdin.readline()
        tmp = [0] * 26
        for j in range(len(word) - 1):
            tmp[ord(word[j]) - 97] = 1
            total[ord(word[j]) - 97] = 1
        table.append(tmp)
    for j in range(26):
        for i in range(N):
            if table[i][j] == 0:
                essential[j] = 0
                break
    if M < sum(essential):
        print(0)
        return
    if M >= sum(total):
        print(N)
        return
    for i in range(N):
        for j in range(26):
            table[i][j] -= essential[j]
            if i == 0:
                total[j] -= essential[j]
    print(getans(M - sum(essential)))


def getans(tWords):
    global table, total, N
    tmp = []
    for i in range(26):
        if total[i]:
            tmp.append(i)
    cases = list(combinations(tmp, tWords))
    ans = 0
    for case in cases:
        std = [0] * 26
        tmp = N
        for idx in case:
            std[idx] = 1
        for word in table:
            for i in range(26):
                if word[i] == 1 and std[i] == 0:
                    tmp -= 1
                    break
        if ans < tmp:
            ans = tmp
    return ans


if __name__ == "__main__":
    main()
