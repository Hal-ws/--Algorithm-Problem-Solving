import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    pos = getballpos(board, N, M)
    red, blue, hole = pos[0], pos[1], pos[2]
    print(bruteforce(board, red, blue, hole))


def getballpos(board, N, M):
    pos = [None, None, None]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                pos[0] = [i, j]
            if board[i][j] == "B":
                pos[1] = [i, j]
            if board[i][j] == "O":
                pos[2] = [i, j]
    return pos


def bruteforce(board, red, blue, hole):
    directions = [0, 0, 0, 0, 0, 0, 0, 0, 0, -1]
    for i in range(4 ** 10):
        directions[9] += 1
        for j in range(10):
            if directions[9 - j] == 4:
                directions[9 - j] = 0
                directions[9 - j - 1] += 1
        if move(board, red, blue, hole, directions):
            return 1  ## 하다가 중간에 되는거 있으면 stop.
    return 0  ## 다 해봤는데 안되면 0 return


def move(board, red, blue, hole, directions):  ## 중간에 파란볼 들어가면 0 return, 빨간볼 들어가면 1 return
    for i in range(10):
        if directions[i] == 0:  ## 상
            if red[0] < blue[0]:
                while board[red[0] - 1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] -= 1
                    board[red[0]][red[1]] = 'R'
                while board[blue[0] - 1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] -= 1
                    board[blue[0]][blue[1]] = 'B'
                if board[red[0] - 1][red[1]] == 'O':
                    return 1
                if board[blue[0] - 1][blue[1]] == 'O':
                    return 0
            else:
                while board[blue[0] - 1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] -= 1
                    board[blue[0]][blue[1]] = 'B'
                while board[red[0] - 1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] -= 1
                    board[red[0]][red[1]] = 'R'
                if board[blue[0] - 1][blue[1]] == 'O':
                    return 0
                if board[red[0] - 1][red[1]] == 'O':
                    return 1
        if directions[i] == 1:  ## 하
            if red[0] > blue[0]:
                while board[red[0] + 1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] += 1
                    board[red[0]][red[1]] = 'R'
                while board[blue[0] + 1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] += 1
                    board[blue[0]][blue[1]] = 'B'
                if board[red[0] + 1][red[1]] == 'O':
                    return 1
                if board[blue[0] + 1][blue[1]] == 'O':
                    return 0
            else:
                while board[blue[0] + 1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] += 1
                    board[blue[0]][blue[1]] = 'B'
                while board[red[0] + 1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] += 1
                    board[red[0]][red[1]] = 'R'
                if board[blue[0] + 1][blue[1]] == 'O':
                    return 0
                if board[red[0] + 1][red[1]] == 'O':
                    return 1
        if directions[i] == 2:  ## 좌
            if red[1] < blue[1]:
                while board[red[0]][red[1] - 1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] -= 1
                    board[red[0]][red[1]] = 'R'
                while board[blue[0]][blue[1] - 1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] -= 1
                    board[blue[0]][blue[1]] = 'B'
                if board[red[0]][red[1] - 1] == 'O':
                    return 1
                if board[blue[0]][blue[1] - 1] == 'O':
                    return 0
            else:
                while board[blue[0]][blue[1] - 1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] -= 1
                    board[blue[0]][blue[1]] = 'B'
                while board[red[0]][red[1] - 1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] -= 1
                    board[red[0]][red[1]] = 'R'
                if board[blue[0]][blue[1] - 1] == 'O':
                    return 0
                if board[red[0]][red[1] - 1] == 'O':
                    return 1
        if directions[i] == 3:  ## 우
            if red[1] < blue[1]:
                while board[blue[0]][blue[1] + 1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] += 1
                    board[blue[0]][blue[1]] = 'B'
                while board[red[0]][red[1] + 1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] += 1
                    board[red[0]][red[1]] = 'R'
                if board[blue[0]][blue[1] + 1] == 'O':
                    return 0
                if board[red[0]][red[1] + 1] == 'O':
                    return 1
            else:
                while board[red[0]][red[1] - 1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] += 1
                    board[red[0]][red[1]] = 'R'
                while board[blue[0]][blue[1] - 1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] += 1
                    board[blue[0]][blue[1]] = 'B'
                if board[red[0]][red[1] - 1] == 'O':
                    return 1
                if board[blue[0]][blue[1] - 1] == 'O':
                    return 0


if __name__ == "__main__":
    main()
