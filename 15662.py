import sys


def main():
    T = int(sys.stdin.readline())
    gears = []
    for i in range(T):
        gears.append((sys.stdin.readline()[:8]))
    K = int(sys.stdin.readline())
    for i in range(K):
        number, direction = map(int, sys.stdin.readline().split())
        rotation(gears, number, direction, 0, T)
    answer = 0
    for i in range(T):
        if gears[i][0] == "1":
            answer += 1
    print(answer)


def rotation(gears, number, direction, motivated, T): ## motivated: 0 처음 회전, 1: 왼쪽 기어에서 돌림, 2: 오른쪽 기어에서 돌림
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
            rotation(gears, number + 1, direction * (-1), 1, T)
    elif number == T:
        if gears[number - 2][2] != gears[number - 1][6] and motivated == 0:
            leftflag = 1
        if direction == 1:
            gears[number - 1] = gears[number - 1][7] + gears[number - 1][:7]
        else:
            gears[number - 1] = gears[number - 1][1:] + gears[number - 1][0]
        if leftflag:
            rotation(gears, number - 1, direction * (-1), 2, T)
    else:
        if gears[number - 2][2] != gears[number - 1][6] and motivated != 1:
            leftflag = 1
        if gears[number - 1][2] != gears[number][6] and motivated != 2:
            rightflag = 1
        if direction == 1:
            gears[number - 1] = gears[number - 1][7] + gears[number - 1][:7]
        else:
            gears[number - 1] = gears[number - 1][1:] + gears[number - 1][0]
        if leftflag:
            rotation(gears, number - 1, direction * (-1), 2, T)
        if rightflag:
            rotation(gears, number + 1, direction * (-1), 1, T)


if __name__ == "__main__":
    main()
