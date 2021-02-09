import sys
from _collections import deque


def main():
    global board, visit
    board = [None] * 33
    board[0] = [0, 0, [1]]
    visit = [[[[0 for j in range(33)] for i in range(33)] for k in range(33)] for l in range(33)]
    for i in range(1, 21):
        board[i] = [0, 2 * i, [i + 1]]
        if i == 5 or i == 10 or i == 15:
            board[i][0] = 1 # blue 표시
    for i in range(3):
        board[21 + i] = [0, 13 + 3 * i, [21 + i + 1]]
        if i == 2:
            board[21 + i][2] = [29]
    board[5][2].append(21)
    board[10][2].append(24)
    board[15][2].append(26)
    board[24] = [0, 22, [25]]
    board[25] = [0, 24, [29]]
    board[26] = [0, 28, [27]]
    board[27] = [0, 27, [28]]
    board[28] = [0, 26, [29]]
    board[29] = [0, 25, [30]]
    board[30] = [0, 30, [31]]
    board[31] = [0, 35, [20]]
    board[20] = [0, 40, [32]]
    board[32] = [0, 0, 0]
    print(bfs())


def bfs():
    global board, visit
    q = deque()
    visit[0][0][0][0] = 1
    dice = list(map(int, sys.stdin.readline().split()))
    q.append([0, 0, 0, 0, 0, 0]) # 네 말 위치, 현재 굴려야하는 주사위 index, score
    ans = 0
    while len(q) > 0:
        status = q[0]
        horses, dIdx, score = [status[0], status[1], status[2], status[3]], status[4], status[5]
        if dIdx == 10:
            if ans < score:
                ans = score
            q.popleft()
            continue
        dis = dice[dIdx]
        for hIdx in range(4):
            pos = horses[hIdx]
            nxt = move(pos, dis, board[pos][0])
            if nxt != 32: #마지막 node가 아니면
                if nxt not in horses:
                    nHorses = [horses[0], horses[1], horses[2], horses[3]]
                    nHorses[hIdx] = nxt
                    if visit[nHorses[0]][nHorses[1]][nHorses[2]][nHorses[3]] == 0:
                        visit[nHorses[0]][nHorses[1]][nHorses[2]][nHorses[3]] = 1
                        q.append(nHorses + [dIdx + 1, score + board[nxt][1]])
            else: # 마지막 노드로 갈때
                nHorses = [horses[0], horses[1], horses[2], horses[3]]
                nHorses[hIdx] = nxt
                if visit[nHorses[0]][nHorses[1]][nHorses[2]][nHorses[3]] == 0:
                    visit[nHorses[0]][nHorses[1]][nHorses[2]][nHorses[3]] = 1
                    q.append(nHorses + [dIdx + 1, score + board[nxt][1]])
        q.popleft()
    return ans


def move(pos, dis, color):
    global board
    if dis == 0: #다 움직임
        return pos
    if pos == 32:
        return pos
    nxt = board[pos][2][color]
    return move(nxt, dis - 1, 0) # 이동하는 중간에는 무조건 red로 간다


if __name__ == '__main__':
    main()
