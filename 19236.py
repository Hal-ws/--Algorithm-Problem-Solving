import sys
from copy import deepcopy


def main():
    global ans, dy, dx
    board = [[[0, 0] for j in range(4)] for i in range(4)]
    fishes = [None] * 17
    dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    ans = 0
    for i in range(4):
        tmp = list(map(int, sys.stdin.readline().split()))
        board[i][0] = tmp[:2] # 물고기 번호, 방향
        fishes[board[i][0][0]] = [i, 0, board[i][0][1]] #물고기 y, x 좌표, 방향 저장
        board[i][1] = tmp[2:4]
        fishes[board[i][1][0]] = [i, 1, board[i][1][1]]
        board[i][2] = tmp[4:6]
        fishes[board[i][2][0]] = [i, 2, board[i][2][1]]
        board[i][3] = tmp[6:8]
        fishes[board[i][3][0]] = [i, 3, board[i][3][1]]
    fishes[board[0][0][0]] = [None, None, None]
    cnt = board[0][0][0]
    board[0][0] = ['s', board[0][0][1]]
    dfs(board, fishes, [0, 0], cnt)
    print(ans)


def fishmove(board, fishes):
    global dy, dx
    for fIdx in range(1, 17):
        if fishes[fIdx] != [None, None, None]:
            d = fishes[fIdx][2]
            y, x = fishes[fIdx][0], fishes[fIdx][1]
            cnt = 0
            while cnt <= 7:
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx][0] != 's': #위치 변경
                    nIdx = board[ny][nx][0] # 교체되는 물고기의 index
                    if nIdx == None: # 빈칸으로 움직일 때
                        board[ny][nx][0], board[ny][nx][1] = board[y][x][0], board[y][x][1]
                        fishes[fIdx] = [ny, nx, d]
                        board[y][x] = [None, None]
                    else: #물고기가 서로 교체될때
                        fishes[fIdx] = [ny, nx, d]
                        fishes[nIdx][0], fishes[nIdx][1] = y, x
                        board[ny][nx] = [fIdx, d]
                        board[y][x] = [nIdx, fishes[nIdx][2]]
                    break
                else:
                    cnt += 1
                    if d == 8:
                        d = 1
                    else:
                        d += 1


def dfs(board, fishes, sPos, cnt):
    global ans, dy, dx
    y, x = sPos[0], sPos[1]
    dir = board[y][x][1]
    flag = 0 # 이동할수 있는지 확인
    fishmove(board, fishes)
    for dis in range(1, 4): # 1칸, 2칸, 3칸 움직임
        ny, nx = y + dy[dir] * dis, x + dx[dir] * dis
        if 0 <= ny < 4 and 0 <= nx < 4:
            if board[ny][nx] != [None, None]: # 잡아먹을수 있음
                flag = 1
                tmpBoard = deepcopy(board)
                tmpFish = deepcopy(fishes)
                tmpBoard[y][x] = [None, None] # 원래 상어가 있던자리는 빈자리가 됨
                fIdx = tmpBoard[ny][nx][0] # 잡아먹힐 물고기의 index
                tmpBoard[ny][nx] = ['s', tmpFish[fIdx][2]] # 잡아먹은 물고기의 방향 가져옴
                tmpFish[fIdx] = [None, None, None]
                dfs(tmpBoard, tmpFish, [ny, nx], cnt + fIdx)
        else: #벗어나면 종료
            break
    if flag == 0: #이동 불가능
        if ans <= cnt:
            ans = cnt


if __name__ == '__main__':
    main()
