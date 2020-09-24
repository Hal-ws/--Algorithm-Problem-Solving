import sys


def main():
    N, M, x, y, K = map(int, sys.stdin.readline().split())
    paper, pos, dice = [], [x, y], [0, 0, 0, 0, 0, 0]
    for i in range(N):
        paper.append(list(map(int, sys.stdin.readline().split())))
    order = list(map(int, sys.stdin.readline().split()))
    for i in range(K):
        ans = movedice(paper, pos, N, M, dice, order[i])
        if ans >= 0:
            print(ans)
    return 0


def movedice(paper, pos, N, M, dice, order):
    if order == 1:
        if pos[1] == M - 1:
            return -1
        pos[1] += 1
    if order == 2:
        if pos[1] == 0:
            return -1
        pos[1] -= 1
    if order == 3:
        if pos[0] == 0:
            return -1
        pos[0] -= 1
    if order == 4:
        if pos[0] == N - 1:
            return -1
        pos[0] += 1
    return rollingdice(paper, dice, pos, order)


def rollingdice(paper, dice, pos, order):
    if order == 1:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    if order == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    if order == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    if order == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    if paper[pos[0]][pos[1]] == 0:
        paper[pos[0]][pos[1]] = dice[0]
    else:
        dice[0] = paper[pos[0]][pos[1]]
        paper[pos[0]][pos[1]] = 0
    return dice[1]


if __name__ == "__main__":
    main()
