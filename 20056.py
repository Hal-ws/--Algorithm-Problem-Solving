import sys


def main():
    global N, fireball, board, dy, dx
    N, M, K = map(int, sys.stdin.readline().split())
    fireball = []
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(M):
        r, c, m, s, d = map(int, sys.stdin.readline().split())
        fireball.append([r - 1, c - 1, m, s, d])
    for k in range(K):
        board = [[[] for j in range(N)] for i in range(N)]
        command()
    ans = 0
    for b in fireball:
        if b != None:
            ans += b[2]
    print(ans)


def command():
    global N, fireball, board
    for bIdx in range(len(fireball)):
        ball = fireball[bIdx]
        if ball != None: # 없어진 fireball 이 아니면
            move(bIdx)
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                disperse([i, j])



def move(bIdx):
    global N, fireball, board, dy, dx
    y, x, s, d = fireball[bIdx][0], fireball[bIdx][1], fireball[bIdx][3], fireball[bIdx][4]
    for cnt in range(s):
        y, x = y + dy[d], x + dx[d]
        if y == -1:
            y = N - 1
        if x == -1:
            x = N - 1
        if y == N:
            y = 0
        if x == N:
            x = 0
    board[y][x].append(bIdx)
    fireball[bIdx][0], fireball[bIdx][1] = y, x


def disperse(pos):
    global N, fireball, board, dy, dx
    sameBalls = board[pos[0]][pos[1]] #같은 위치에 있는 ball들의 idx
    tmp = []
    sumM = 0
    sumSpeed = 0
    flag = -1 # 방향 설정
    cnt = 0
    for bIdx in sameBalls:
        cnt += 1
        tmp.append(bIdx)
        sumM += fireball[bIdx][2]
        sumSpeed += fireball[bIdx][3]
        if flag == -1:
            dflag = fireball[bIdx][4] % 2 #dflag가 0이면 짝수, 1이면 홀수
            flag = 1
        if dflag != fireball[bIdx][4] % 2:
            flag = 0 # 중간에 다른 방향이 섞임
    if sumM >= 5:
        newM = sumM // 5
        newS = sumSpeed // cnt
        if flag: # 짝수방향으로 진행
            for nd in range(0, 8, 2):
                fireball.append([pos[0], pos[1], newM, newS, nd])
        else:
            for nd in range(1, 8, 2):
                fireball.append([pos[0], pos[1], newM, newS, nd])
    for dIdx in tmp:
        fireball[dIdx] = None


if __name__ == '__main__':
    main()
