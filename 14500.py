import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    pieceList = []
    pieceList.append([[1, 1, 1, 1]])
    pieceList.append([[1, 1], [1, 1]])
    pieceList.append([[1, 0], [1, 0], [1, 1]])
    pieceList.append([[0, 1], [0, 1], [1, 1]])
    pieceList.append([[1, 0], [1, 1], [0, 1]])
    pieceList.append([[0, 1], [1, 1], [1, 0]])
    pieceList.append([[1, 1, 1], [0, 1, 0]])
    ans = 0
    for piece in pieceList:
        for _ in range(4):
            piece = rotation(piece)
            h, w = len(piece), len(piece[0])
            for sY in range(N - h + 1):
                for sX in range(M - w + 1):
                    tmpAns = 0
                    for i in range(h):
                        for j in range(w):
                            tmpAns += piece[i][j] * board[sY + i][sX + j]
                    ans = max(ans, tmpAns)
    print(ans)


def rotation(piece):
    h, w = len(piece), len(piece[0])
    newPiece = [[0 for j in range(h)] for i in range(w)]
    for i in range(w):
        for j in range(h):
            newPiece[i][j] = piece[h - 1 - j][i]
    return newPiece


if __name__ == "__main__":
    main()
