import sys


def main():
    R, C, T = map(int, sys.stdin.readline().split())
    room = []
    for i in range(R):
        room.append(list(map(int, sys.stdin.readline().split())))
    for i in range(C):
        if room[i][0] == -1:
            acPos = i
            break
    for i in range(T):
        disperse(room, R, C)
        for j in range(R):
            print(room[j])
        print('-----------------------------------------')
        circulation(room, R, C, acPos)
        for j in range(R):
            print(room[j])
        print('-----------------------------------------')
    ans = 0
    for i in range(R):
        ans += sum(room[i])
    print(ans + 2)


def disperse(room, R, C):
    variance = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] > 1:
                if i > 0 and room[i - 1][j] != -1:
                    variance[i - 1][j] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
                if i < R - 1 and room[i + 1][j] != -1:
                    variance[i + 1][j] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
                if j > 0 and room[i][j - 1] != -1:
                    variance[i][j - 1] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
                if j < C - 1 and room[i][j + 1] != -1:
                    variance[i][j + 1] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
    for i in range(R):
        for j in range(C):
            room[i][j] += variance[i][j]


def circulation(room, R, C, acPos):
    rB, ruB, luB = 0, 0, 0
    if room[acPos][C - 1] != 0:
        rB = room[acPos][C - 1]
    rightmove(room, C, acPos)
    if room[0][C - 1] != 0:
        ruB = room[0][C - 1]
    upmove(room, C, acPos, rB)
    if room[0][0] != 0:
        luB = room[0][0]
    leftmove(room, C, ruB)
    downmove(room, acPos, luB)
    rB, rdB, ldB = 0, 0, 0
    if room[acPos + 1][C - 1] != 0:
        rB = room[acPos + 1][C - 1]
    rightmove(room, C, acPos + 1)
    if room[R - 1][C - 1] != 0:
        rdB = room[R - 1][C - 1]
    rightdown(room, acPos + 1, rB, R, C)
    if room[R - 1][0] != 0:
        ldB = room[R - 1][0]
    leftdown(room, R, C, rdB)
    upleft(room, R, acPos + 1, ldB)


def rightmove(room, C, acPos):
    for i in range(C - 1, 0, -1):
        if i != 1:
            room[acPos][i] = room[acPos][i - 1]
        else:
            room[acPos][i] = 0


def upmove(room, C, acPos, rB):
    for i in range(0, acPos):
        if i == acPos - 1:
            room[i][C - 1] = rB
        else:
            room[i][C - 1] = room[i + 1][C - 1]


def leftmove(room, C, ruB):
    for i in range(0, C - 1):
        if i == C - 2:
            room[0][i] = ruB
        else:
            room[0][i] = room[0][i + 1]


def downmove(room, acPos, lub):
    for i in range(1, acPos):
        if i == 1:
            room[i][0] = lub
        else:
            room[i][0] = room[i - 1][0]


def leftdown(room, R, C, rdB):
    for i in range(0, C - 1):
        if i == C - 2:
            room[R - 1][i] = rdB
        else:
            room[R - 1][i] = room[R - 1][i + 1]


def upleft(room, R, acPos, ldB):
    for i in range(acPos + 1, R - 1):
        if i == R - 2:
            room[i][0] = ldB
        else:
            room[i][0] = room[i + 1][0]



def rightdown(room, acPos, rB, R, C):
    for i in range(R - 1, acPos, - 1):
        if i == acPos + 1:
            room[i][C - 1] = rB
        else:
            room[i][C - 1] = room[i - 1][C - 1]


if __name__ == "__main__":
    main()
