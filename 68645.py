def solution(n):
    answer = []
    board = [[0 for j in range(2 * n - 1)] for i in range(n)]
    y, x = 0, n - 1
    cnt, d = 1, 0
    while cnt <= n * (n + 1) // 2:
        board[y][x] = cnt
        if d == 0:
            if y <= n - 2 and board[y + 1][x - 1] == 0:
                y, x = y + 1, x - 1
            else:
                d = 1
                x += 2
        elif d == 1:
            if x <= 2 * y - 2 and board[y][x + 2] == 0:
                x += 2
            else:
                d = 2
                y, x = y - 1, x - 1
        elif d == 2:
            if y > 0 and board[y - 1][x - 1] == 0:
                y, x = y - 1, x - 1
            else:
                d = 0
                y, x = y + 1, x - 1
        cnt += 1
    for i in range(n):
        for j in range(2 * n - 1):
            if board[i][j] != 0:
                answer.append(board[i][j])
    return answer
