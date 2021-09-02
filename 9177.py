import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    for i in range(N):
        print("Data set %s: " %(i + 1), end='')
        word1, word2, word3 = map(str, sys.stdin.readline().split())
        if chkPossible(word1, word2, word3):
            print("yes")
        else:
            print("no")


def chkPossible(word1, word2, word3):  # word1과 word2로 word3를 만들 수 있는지 확인
    l1, l2 = len(word1), len(word2)
    visit = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
    visit[0][0] = 0
    q = deque()
    q.append([0, 0, 0])
    while len(q) > 0:
        tmp = q.popleft()
        idx1, idx2, idx3 = tmp[0], tmp[1], tmp[2]
        if idx1 == l1 and idx2 == l2:
            return 1
        if idx1 < len(word1) and idx2 < len(word2):
            if word1[idx1] == word3[idx3] and visit[idx1 + 1][idx2] == 0:
                q.append([idx1 + 1, idx2, idx3 + 1])
                visit[idx1 + 1][idx2] = 1
            if word2[idx2] == word3[idx3] and visit[idx1][idx2 + 1] == 0:
                q.append([idx1, idx2 + 1, idx3 + 1])
                visit[idx1][idx2 + 1] = 1
        else:
            if idx1 < len(word1):
                if word1[idx1] == word3[idx3] and visit[idx1 + 1][idx2] == 0:
                    q.append([idx1 + 1, idx2, idx3 + 1])
                    visit[idx1 + 1][idx2] = 1
            else:
                if word2[idx2] == word3[idx3] and visit[idx1][idx2 + 1] == 0:
                    q.append([idx1, idx2 + 1, idx3 + 1])
                    visit[idx1][idx2 + 1] = 1
    return 0


if __name__ == "__main__":
    main()
