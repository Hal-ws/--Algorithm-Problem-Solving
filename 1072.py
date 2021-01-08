import sys


def main():
    X, Y = map(int, sys.stdin.readline().split())
    cRate = int((Y * 100 / X))
    if cRate == 99 or cRate == 100:
        V = -1
    else:
        nocng = 0
        mincng = 1000000001
        V = 1
        while 1:
            tmpRate = int(((Y + V) * 100 / (X + V)))
            cng = tmpRate - cRate
            if cng == 0:
                if nocng <= V:
                    nocng = V
                V *= 2
            else:
                if V == nocng + 1:
                    break
                if V <= mincng:
                    mincng
                V = (nocng + V) // 2
    print(V)


if __name__ == '__main__':
    main()
