def main():
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(str, input())))
    ans = 0
    for i in range(N):
        temp = max(countgaro(board, i, N), countsero(board, i, N))
        if temp > ans:
            ans = temp
    for i in range(N):
        for j in range(N - 1):
            garoswap(board, i, j)
            temp = countgaro(board, i, N)
            if temp > ans:
                ans = temp
            temp = countsero(board, j, N)
            if temp > ans:
                ans = temp
            temp = countsero(board, j + 1, N)
            if temp > ans:
                ans = temp
            garoswap(board, i, j)
    for i in range(N - 1):
        for j in range(N):
            seroswap(board, i, j)
            temp = countsero(board, j, N)
            if temp > ans:
                ans = temp
            temp = countgaro(board, i, N)
            if temp > ans:
                ans = temp
            temp = countgaro(board, i + 1, N)
            if temp > ans:
                ans = temp
            seroswap(board, i, j)
    print(ans)



def garoswap(board, y, x): ## 가로 swap 후 swap 해준 대상에 대해서만 countsero를 해준다
    board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]


def seroswap(board, y, x):
    board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]


def countgaro(board, idx, N):
    maxLen = [[0, 0], [0, 0], [0, 0], [0, 0]]  # C, P, Z, Y 캔디의 각각 최대 길이, temp값 저장
    for i in range(N - 1):
        if board[idx][i] == "C":
            garolen(board, maxLen, i, idx, N, "C", 0)
        if board[idx][i] == "P":
            garolen(board, maxLen, i, idx, N, "P", 1)
        if board[idx][i] == "Z":
            garolen(board, maxLen, i, idx, N, "Z", 2)
        if board[idx][i] == "Y":
            garolen(board, maxLen, i, idx, N, "Y", 3)
    result = 0
    for i in range(4):
        if maxLen[i][0] >= result:
            result = maxLen[i][0]
    return result


def countsero(board, idx, N): # j = idx에서 최대연속점을 고름
    maxLen = [[0, 0], [0, 0], [0, 0], [0, 0]] #C, P, Z, Y 캔디의 각각 최대 길이, temp값 저장
    for i in range(N - 1):
        if board[i][idx] == "C":
            serolen(board, maxLen, i, idx, N, "C", 0)
        if board[i][idx] == "P":
            serolen(board, maxLen, i, idx, N, "P", 1)
        if board[i][idx] == "Z":
            serolen(board, maxLen, i, idx, N, "Z", 2)
        if board[i][idx] == "Y":
            serolen(board, maxLen, i, idx, N, "Y", 3)
    result = 0
    for i in range(4):
        if maxLen[i][0] >= result:
            result = maxLen[i][0]
    return result


def garolen(board, maxLen, i, idx, N, candy, lenIdx):
    maxLen[lenIdx][1] += 1
    if board[idx][i + 1] != candy:  # 더 연속되지 않고 끊김.
        if maxLen[lenIdx][0] < maxLen[lenIdx][1]:
            maxLen[lenIdx][0] = maxLen[lenIdx][1]
        maxLen[lenIdx][1] = 0
    if i + 1 == N - 1 and board[idx][i + 1] == candy:  # 마지막까지 연결됨
        maxLen[lenIdx][1] += 1
        if maxLen[lenIdx][0] < maxLen[lenIdx][1]:
            maxLen[lenIdx][0] = maxLen[lenIdx][1]
        maxLen[lenIdx][1] = 0


def serolen(board, maxLen, i, idx, N, candy, lenIdx):
    maxLen[lenIdx][1] += 1
    if board[i + 1][idx] != candy: #더 연속되지 않고 끊김.
        if maxLen[lenIdx][0] < maxLen[lenIdx][1]:
            maxLen[lenIdx][0] = maxLen[lenIdx][1]
        maxLen[lenIdx][1] = 0
    if i + 1 == N - 1 and board[i + 1][idx] == candy: #마지막까지 연결됨
        maxLen[lenIdx][1] += 1
        if maxLen[lenIdx][0] < maxLen[lenIdx][1]:
            maxLen[lenIdx][0] = maxLen[lenIdx][1]
        maxLen[lenIdx][1] = 0


if __name__ == "__main__":
    main()
