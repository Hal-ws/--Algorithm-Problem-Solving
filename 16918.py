import sys


def main():
    R, C, N = map(int, sys.stdin.readline().split())
    blocks = []
    for i in range(R):
        blocks.append(list(sys.stdin.readline()[:C]))
    for i in range(R):
        for j in range(C):
            if blocks[i][j] == "O":
                blocks[i][j] = 2
            else:
                blocks[i][j] = -1 # 폭탄 없는건 -1
    for i in range(R):
        for j in range(C):
            if blocks[i][j] != 2:
                blocks[i][j] = 0
    time = 3
    if N > 1:
        while time <= N:
            if time % 2 == 0:
                setbomb(blocks, R, C)
            else:
                explosion(blocks, R, C)
            time += 1
        for i in range(R):
            for j in range(C):
                if blocks[i][j] != -1:
                    print('O', end='')
                else:
                    print('.', end='')
            print()
    else:
        for i in range(R):
            for j in range(C):
                if blocks[i][j] == 2:
                    print('O', end='')
                else:
                    print('.', end='')
            print()


def explosion(blocks, R, C):
    for i in range(R):
        for j in range(C):
            if blocks[i][j] != -1:
                blocks[i][j] += 1
            if blocks[i][j] == 3: # 설치한지 3초지난 폭탄 발견
                blocks[i][j] = -1 # 폭발해서 폭탄 없어짐
                if i > 0 and blocks[i - 1][j] != 2:
                    blocks[i - 1][j] = -1
                if i < R - 1 and blocks[i + 1][j] != 2:
                    blocks[i + 1][j] = -1
                if j > 0 and blocks[i][j - 1] != 2:
                    blocks[i][j - 1] = -1
                if j < C - 1 and blocks[i][j + 1] != 2:
                    blocks[i][j + 1] = -1


def setbomb(blocks, R, C):
    for i in range(R):
        for j in range(C):
            if blocks[i][j] != 0:
                blocks[i][j] += 1
            else:
                blocks[i][j] = 1


if __name__ == "__main__":
    main()
