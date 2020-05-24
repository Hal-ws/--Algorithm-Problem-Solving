import sys

board = ['......',
         '......',
         '..WB..',
         '..BW..',
         '......',
         '......']

def changeStones(pos, direction, board):
    color = board[pos[0]][pos[1]]
    for i in range(len(direction)):
        j = 1
        while True:
            board[pos[0] + direction[i] * j][pos[1] + direction[i] * j] = color
            if board[pos[0] + direction[i] * (j + 1)][pos[1] + direction[i] * (j + 1)] == color:
                break
            j += 1
    return board

def getdirection(pos, board):
    stoneColor = board[pos[0]][pos[1]]
    directions = []
    if pos[0] == 0 and pos[1] == 0:
        flag = 0
        for i in range(1, 6):
            if board[0][i] == '.':
                break
            elif stoneColor == board[0][i]:
                flag = 1
                break
        if flag == 1:
            directions.append([0, 1])
        


    return directions

N = int(sys.stdin.readline())

for i in range(N):
    R, C = map(int, sys.stdin.readline().split())
    if i % 2 == 0:
        board[R - 1][C - 1] = 'B'
    else:
        board[R - 1][C - 1] = 'W'
    directions = getdirection([R - 1, C - 1], board)
    board = changeStones([R - 1, C - 1], directions, board)

for i in range(N):
    print(board[i])

blackSum = 0
whiteSum = 0
for i in range(N):
    blackSum += board[i].count('B')
    blackSum += board[i].count('W')

if blackSum > whiteSum:
    print('Black')
else:
    print('White')
