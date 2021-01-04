from collections import deque
from itertools import permutations
import sys


def main():
    global N, M, ans
    ans = 5001
    N, M, K = map(int, sys.stdin.readline().split())
    board, r = [], []
    rnum = [i for i in range(K)]
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(K):
        r.append(list(map(int, sys.stdin.readline().split())))
    cases = list(permutations(rnum))
    for case in cases:
        tmp = []
        for i in range(N):
            tmp.append(board[i][:])
        for order in case:
            rotation(tmp, r[order])
        tmpAns = 5001
        for i in range(N):
            tmpSum = sum(tmp[i])
            if tmpSum <= tmpAns:
                tmpAns = tmpSum
        if tmpAns <= ans:
            ans = tmpAns
    print(ans)


def rotation(tmp, info):
    r, c, s = info[0] - 1, info[1] - 1, info[2]
    for layer in range(s + 1):
        lu = [r - layer, c - layer]
        rd = [r + layer, c + layer]
        q = deque()
        for j in range(lu[1], rd[1] + 1):
            q.append(tmp[lu[0]][j])
        for i in range(lu[0] + 1, rd[0] + 1):
            q.append(tmp[i][rd[1]])
        for j in range(rd[1] - 1, lu[1] - 1, - 1):
            q.append(tmp[rd[0]][j])
        for i in range(rd[0] - 1, lu[0], -1):
            q.append(tmp[i][lu[1]])
        q.appendleft(q.pop())
        for j in range(lu[1], rd[1] + 1):
            tmp[lu[0]][j] = q.popleft()
        for i in range(lu[0] + 1, rd[0] + 1):
            tmp[i][rd[1]] = q.popleft()
        for j in range(rd[1] - 1, lu[1] - 1, - 1):
            tmp[rd[0]][j] = q.popleft()
        for i in range(rd[0] - 1, lu[0], -1):
            tmp[i][lu[1]] = q.popleft()


if __name__ == '__main__':
    main()
