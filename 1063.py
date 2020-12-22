import sys


def main():
    king, stone, N = map(str, sys.stdin.readline().split())
    N = int(N)
    king = [8 - int(king[1]), ord(king[0]) - 65]
    stone = [8 - int(stone[1]), ord(stone[0]) - 65]
    for i in range(N):
        command = sys.stdin.readline()
        ky, kx = king[0], king[1]
        sy, sx = stone[0], stone[1]
        if command == "R\n":
            if ky == sy and kx + 1 == sx: #같은곳으로 움직일때
                if kx + 1 < 8 and sx + 1 < 8:
                    king = [ky, kx + 1]
                    stone = [sy, sx + 1]
            else:
                if kx + 1 < 8:
                    king = [ky, kx + 1]
        if command == "L\n":
            if ky == sy and kx - 1 == sx:
                if 0 <= kx - 1 and 0 <= sx - 1:
                    king = [ky, kx - 1]
                    stone = [sy, sx - 1]
            else:
                if 0 <= kx - 1:
                    king = [ky, kx - 1]
        if command == "B\n":
            if ky + 1 == sy and kx == sx:
                if ky + 1 < 8 and sy + 1 < 8:
                    king = [ky + 1, kx]
                    stone = [sy + 1, sx]
            else:
                if ky + 1 < 8:
                    king = [ky + 1, kx]
        if command == "T\n":
            if ky - 1 == sy and kx == sx:
                if 0 <= ky - 1 and 0 <= sy - 1:
                    king = [ky - 1, kx]
                    stone = [sy - 1, sx]
            else:
                if 0 <= ky - 1:
                    king = [ky - 1, kx]
        if command == "RT\n":
            if ky - 1 == sy and kx + 1 == sx:
                if 0 <= ky - 1 and 0 <= sy - 1 and kx + 1 < 8 and sx + 1 < 8:
                    king = [ky - 1, kx + 1]
                    stone = [sy - 1, sx + 1]
            else:
                if 0 <= ky - 1 and kx + 1 < 8:
                    king = [ky - 1, kx + 1]
        if command == "LT\n":
            if ky - 1 == sy and kx - 1 == sx:
                if 0 <= ky - 1 and 0 <= sy - 1 and 0 <= kx - 1 and 0 <= sx - 1:
                    king = [ky - 1, kx - 1]
                    stone = [sy - 1, sx - 1]
            else:
                if 0 <= ky - 1 and 0 <= kx - 1:
                    king = [ky - 1, kx - 1]
        if command == "RB\n":
            if ky + 1 == sy and kx + 1 == sx:
                if kx + 1 < 8 and sx + 1 < 8 and ky + 1 < 8 and sy + 1 < 8:
                    king = [ky + 1, kx + 1]
                    stone = [sy + 1, sx + 1]
            else:
                if ky + 1 < 8 and kx + 1 < 8:
                    king = [ky + 1, kx + 1]
        if command == "LB\n":
            if ky + 1 == sy and kx - 1 == sx:
                if 0 <= kx - 1 and 0 <= sx - 1 and ky + 1 < 8 and sy + 1 < 8:
                    king = [ky + 1, kx - 1]
                    stone = [sy + 1, sx - 1]
            else:
                if ky + 1 < 8 and 0 <= kx - 1:
                    king = [ky + 1, kx - 1]
    king = chr(king[1] + 65) + str(8 - king[0])
    stone = chr(stone[1] + 65) + str(8 - stone[0])
    print(king)
    print(stone)


if __name__ == '__main__':
    main()
