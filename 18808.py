import sys


def main():
    global N, M
    N, M, K= map(int, sys.stdin.readline().split())
    board = [[0 for j in range(M)] for i in range(N)]
    answer = 0
    for _ in range(K):
        R, C = map(int, sys.stdin.readline().split())
        sticker = []
        for i in range(R):
            sticker.append(list(map(int, sys.stdin.readline().split())))
        for i in range(4):
            if putSticker(sticker, board, R, C):
                break
            else:
                sticker = rotation(R, C, sticker)
                C, R = R, C # 회전했으니 스티커의 가로, 세로 변경
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                answer += 1
    print(answer)


def rotation(R, C, sticker):
    newSticker = [[0 for j in range(R)] for i in range(C)]
    for i in range(R):
        for j in range(C):
            newSticker[j][R - i - 1] = sticker[i][j]
    return newSticker


def putSticker(sticker, board, R, C): # board를 sticker에 붙임
    global N, M
    for i in range(N - R + 1):
        for j in range(M - C + 1): # 시작 좌표
            flag = 1
            marking = []
            for dy in range(R):
                for dx in range(C):
                    y, x = i + dy, j + dx
                    if sticker[dy][dx] == 1:
                        if board[y][x] == 0:
                            marking.append([y, x])
                        else:
                            flag = 0 # 배치 실패
            if flag:
                for pos in marking:
                    board[pos[0]][pos[1]] = 1
                return 1
    return 0


if __name__ == '__main__':
    main()
