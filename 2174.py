import sys


def main():
    global board, A, B
    A, B = map(int, sys.stdin.readline().split())
    N, M = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(A)] for i in range(B)]
    rList = [0 for i in range(N + 1)] # 0번은 더미. 좌표 및 방향 저장
    for i in range(1, N + 1):
        x, y, d = map(str, sys.stdin.readline().split())
        x, y = int(x), int(y)
        y = B - y
        x = x - 1
        board[y][x] = i
        rList[i] = [y, x, d]
    for i in range(M):
        robot, command, repeat = map(str, sys.stdin.readline().split())
        robot, repeat = int(robot), int(repeat)
        if command == 'F':
            result = move(robot, rList, repeat)
            if result != 1:
                print(result)
                return
        if command == 'L' or command == 'R':
            for _ in range(repeat):
                rList[robot][2] = rotation(robot, command, rList)
    print('OK')


def move(robot, rList, dis): # dis만큼 이동
    global board, A, B
    y, x, d = rList[robot][0], rList[robot][1], rList[robot][2]
    if d == 'E':
        for i in range(dis):
            x += 1
            if x == A: #밖으로 나감
                return 'Robot ' + str(robot) + ' crashes into the wall'
            if board[y][x] != 0: #
                return 'Robot ' + str(robot) + ' crashes into robot ' + str(board[y][x])
            board[y][x], board[y][x - 1] = board[y][x - 1], board[y][x]
            rList[robot][0], rList[robot][1] = y, x
    if d == 'W':
        for i in range(dis):
            x -= 1
            if x == -1: #밖으로 나감
                return 'Robot ' + str(robot) + ' crashes into the wall'
            if board[y][x] != 0: #
                return 'Robot ' + str(robot) + ' crashes into robot ' + str(board[y][x])
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            rList[robot][0], rList[robot][1] = y, x
    if d == 'N':
        for i in range(dis):
            y -= 1
            if y == -1:
                return 'Robot ' + str(robot) + ' crashes into the wall'
            if board[y][x] != 0: #
                return 'Robot ' + str(robot) + ' crashes into robot ' + str(board[y][x])
            board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]
            rList[robot][0], rList[robot][1] = y, x
    if d == 'S':
        for i in range(dis):
            y += 1
            if y == B:
                return 'Robot ' + str(robot) + ' crashes into the wall'
            if board[y][x] != 0: #
                return 'Robot ' + str(robot) + ' crashes into robot ' + str(board[y][x])
            board[y][x], board[y - 1][x] = board[y - 1][x], board[y][x]
            rList[robot][0], rList[robot][1] = y, x
    return 1


def rotation(robot, d, rList):
    cur = rList[robot][2]
    if d == 'L':
        if cur == 'W':
            cur = 'S'
        elif cur == 'S':
            cur = 'E'
        elif cur == 'E':
            cur = 'N'
        elif cur == 'N':
            cur = 'W'
    else:
        if cur == 'W':
            cur = 'N'
        elif cur == 'N':
            cur = 'E'
        elif cur == 'E':
            cur = 'S'
        elif cur == 'S':
            cur = 'W'
    return cur


if __name__ == '__main__':
    main()
