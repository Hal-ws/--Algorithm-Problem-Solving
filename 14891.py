import sys


def main():
    gears = []
    for i in range(4):
        gears.append((sys.stdin.readline()[:8]))
    K = int(sys.stdin.readline())
    for i in range(K):
        number, direction = map(int, sys.stdin.readline().split())
        rotation(gears, number, direction, 0)
    answer = 0
    for i in range(4):
        if gears[i][0] == "1":
            answer += 2 ** i
    print(answer)


def rotation(gears, number, direction, motivated): ## motivated: 0 처음 회전, 1: 왼쪽 기어에서 돌림, 2: 오른쪽 기어에서 돌림
    leftflag = 0
    rightflag = 0
    if number == 1:
        if gears[0][2] != gears[1][6] and motivated == 0:
            rightflag = 1
        if direction == 1:
            gears[0] = gears[0][7] + gears[0][:7]
        else:
            gears[0] = gears[0][1:] + gears[0][0]
        if rightflag:
            rotation(gears, number + 1, direction * (-1), 1)
    if number == 2:
        if gears[0][2] != gears[1][6] and motivated != 1:
            leftflag = 1
        if gears[1][2] != gears[2][6] and motivated != 2:
            rightflag = 1
        if direction == 1:
            gears[1] = gears[1][7] + gears[1][:7]
        else:
            gears[1] = gears[1][1:] + gears[1][0]
        if leftflag:
            rotation(gears, number - 1, direction * (-1), 2)
        if rightflag:
            rotation(gears, number + 1, direction * (-1), 1)
    if number == 3:
        if gears[1][2] != gears[2][6] and motivated != 1:
            leftflag = 1
        if gears[2][2] != gears[3][6] and motivated != 2:
            rightflag = 1
        if direction == 1:
            gears[2] = gears[2][7] + gears[2][:7]
        else:
            gears[2] = gears[2][1:] + gears[2][0]
        if leftflag:
            rotation(gears, number - 1, direction * (-1), 2)
        if rightflag:
            rotation(gears, number + 1, direction * (-1), 1)
    if number == 4:
        if gears[2][2] != gears[3][6] and motivated == 0:
            leftflag = 1
        if direction == 1:
            gears[3] = gears[3][7] + gears[3][:7]
        else:
            gears[3] = gears[3][1:] + gears[3][0]
        if leftflag:
            rotation(gears, number - 1, direction * (-1), 2)


if __name__ == "__main__":
    main()
