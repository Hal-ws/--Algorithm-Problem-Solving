import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    chk = [[0 for j in range(N)] for i in range(N)] #수명 기록
    maxDay = 0
    for i in range(N):
        for j in range(N):
            if chk[i][j] == 0:
                dfs(board, chk, [i, j], 1, N)
                if maxDay <= chk[i][j]:
                    maxDay = chk[i][j]
    print(maxDay)


def dfs(board, chk, pos, day, N): #day: 현재 시간
    y, x = pos[0], pos[1]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    flag = 0
    maxDay = 0 #
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and board[y][x] < board[ny][nx]:
            if chk[ny][nx] == 0: #아직 방문 안해서 길이를 구해야함
                flag = 1
                tmpDay = dfs(board, chk, [ny, nx], day, N)
            else: #이미 방문해서 길이를 구한곳임
                flag = 1
                tmpDay = chk[ny][nx]
            if maxDay <= day + tmpDay:
                maxDay = day + tmpDay
    if flag:
        chk[y][x] = maxDay
        return maxDay
    else: #주변에 더 이상 방문할곳이 없음. 길이 0
        chk[y][x] = 1
        return 1


if __name__ == '__main__':
    main()
