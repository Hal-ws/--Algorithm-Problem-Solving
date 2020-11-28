import sys


def main():
    R, C = map(int, sys.stdin.readline().split())
    board = []
    for i in range(R):
        board.append(list(map(str, sys.stdin.readline())))
    flag = 1 # 불가능할땐 flag 0으로 변경함
    for i in range(R):
        for j in range(C):
            if board[i][j] == "W":
                if i > 0:
                    if board[i - 1][j] == "S":
                        flag = 0
                        break
                    if board[i - 1][j] == ".":
                        board[i - 1][j] = "D"
                if i < R - 1:
                    if board[i + 1][j] == "S":
                        flag = 0
                        break
                    if board[i + 1][j] == ".":
                        board[i + 1][j] = "D"
                if j > 0:
                    if board[i][j - 1] == "S":
                        flag = 0
                        break
                    if board[i][j - 1] == ".":
                        board[i][j - 1] = "D"
                if j < C - 1:
                    if board[i][j + 1] == "S":
                        flag = 0
                        break
                    if board[i][j + 1] == ".":
                        board[i][j + 1] = "D"
        if flag == 0:
            break
    if flag:
        print(1)
        for i in range(R):
            for j in range(C):
                print(board[i][j], end='')
            print()
    else:
        print(0)


if __name__ == "__main__":
    main()
