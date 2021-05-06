import sys


def main():
    iniH = 1000000
    curH = 1000000
    minH = 1000000 # 전투 진행 중 닿게 되는 최소 체력
    N, hAtk = map(int, sys.stdin.readline().split())
    rooms = [None] # 0번은 dummy
    for i in range(N):
        rooms.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, N + 1):
        tmp = rooms[i]
        t, a, h = tmp[0], tmp[1], tmp[2]
        if t == 1:
            curH = battle(curH, hAtk, a, h)
        if t == 2:
            hAtk += a
            curH += h
            if curH >= iniH:
                curH = iniH
        if curH <= minH:
            minH = curH
    print(iniH - minH + 1)


def battle(curH, hAtk, a, h): # a, h: 몬스터 공격력, 몬스터 체력
    if h % hAtk == 0:
        cnt = h // hAtk
    else:
        cnt = h // hAtk + 1
    return curH - a * (cnt - 1)


if __name__ == '__main__':
    main()
