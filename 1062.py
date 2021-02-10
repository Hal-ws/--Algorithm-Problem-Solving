from itertools import combinations
import sys


def main():
    global masking, N, M
    N, M = map(int, sys.stdin.readline().split())
    table = []
    total = [0] * 26
    essential = [-1] * 26
    for i in range(N):
        word = sys.stdin.readline()
        tmp = [0] * 26
        for j in range(len(word) - 1):
            tmp[ord(word[j]) - 97] = 1
            total[ord(word[j]) - 97] = 1
        table.append(tmp)
    for i in range(N):
        print(table[i])
    print(total)


def getans(case):
    global masking, N, M
    std = [0] * 26
    for num in case:
        std[num] = 1
    cnt = 0
    for i in range(N):
        flag = 1
        for j in range  (26):
            if masking[i][j] == 1: #j번째 알파벳이 필요함
                if std[j] == 0:
                    flag = 0
        if flag:
            cnt += 1
    return cnt


if __name__ == "__main__":
    main()
