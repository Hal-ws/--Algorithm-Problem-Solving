import sys


def main():
    global dy, dx, ans
    dy, dx = [-1, -1, 0, 0, 1, 1], [-1, 1, -2, 2, -1, 1]
    board = []
    chk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 사용한 것
    ans = 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL'
    xCnt = 0 # 남아있는 x개를 센다. dfs에서 0이 되면 마무리
    for i in range(5):
        board.append(list(sys.stdin.readline()[:9]))
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'x':
                xCnt += 1
            elif board[i][j] != '.':
                chk[ord(board[i][j]) - 65] = 1
    print(chk)


def dfs(board, d, chk, y, x):

    return 0


if __name__ == '__main__':
    main()
