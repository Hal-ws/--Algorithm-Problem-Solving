import sys


def main():
    board = []
    for i in range(3):
        board.append(list(map(int, sys.stdin.readline().split())))
    magics = [[2, 7, 6, 9, 5, 1, 4, 3, 8],
              [2, 9, 4, 7, 5, 3, 6, 1, 8],
              [4, 3, 8, 9, 5, 1, 2, 7, 6],
              [4, 9, 2, 3, 5, 7, 8, 1, 6],
              [6, 1, 8, 7, 5, 3, 2, 9, 4],
              [6, 7, 2, 1, 5, 9, 8, 3, 4],
              [8, 1, 6, 3, 5, 7, 4, 9, 2],
              [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    minPrice = 81
    for case in magics:
        tmpP = 0
        tmpP += abs(board[0][0] - case[0])
        tmpP += abs(board[0][1] - case[1])
        tmpP += abs(board[0][2] - case[2])
        tmpP += abs(board[1][0] - case[3])
        tmpP += abs(board[1][1] - case[4])
        tmpP += abs(board[1][2] - case[5])
        tmpP += abs(board[2][0] - case[6])
        tmpP += abs(board[2][1] - case[7])
        tmpP += abs(board[2][2] - case[8])
        if tmpP < minPrice:
            minPrice = tmpP
    print(minPrice)


if __name__ == '__main__':
    main()
