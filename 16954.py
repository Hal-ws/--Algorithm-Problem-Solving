import sys

def main():
    board = []
    for i in range(8):
        board.append(list(map(str, sys.stdin.readline()[:8])))
    board[7][0] = 'O' #욱제
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    while 1:
        # 욱제가 움직일 수 있는 위치 표시
        chk = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "O":
                    if chk[i][j] == 0:  # 퍼진게 또 퍼지는게 아님.
                        for k in range(8):
                            if 0 <= i + dy[k] < 8 and 0 <= j + dx[k] < 8 and board[i + dy[k]][j + dx[k]] == ".":
                                board[i + dy[k]][j + dx[k]] = "O"
                                chk[i + dy[k]][j + dx[k]] = 1  # 새로 방문한 곳에 표시
                    chk[i][j] = 1
        if board[0][7] == "O": #도착한거 확인했으면 종료
            print(1)
            return 0
        #이제 벽 움직이기 시작함

        wallCnt = 0
        for i in range(7, -1, -1):
            for j in range(8):
                if board[i][j] == "#":
                    if i < 7:
                        board[i + 1][j] = "#"
                    board[i][j] = "."
                    wallCnt += 1
        wallCnt, oCnt = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "#":
                    wallCnt += 1
                if board[i][j] == "O":
                    oCnt += 1
        if wallCnt == 0 and oCnt > 0: #벽은 없는데 욱제는 남아있어도 종료
            print(1)
            return 0
        if oCnt == 0:
            print(0)
            return 0


if __name__ == "__main__":
    main()
