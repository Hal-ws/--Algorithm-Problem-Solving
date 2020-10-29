def main():
    cube = list(map(int, input().split()))
    sf = []
    for i in range(0, 21, 4):
        sf.append(cube[i:i + 4])
    flag = 0
    if flag == 0:
        uc(sf)
        if anschk(sf):
            flag = 1
        else:
            uc(sf)
            uc(sf)
        if anschk(sf):
            flag = 1
    uc(sf) # 원상복구
    if flag == 0:
        fc(sf)
        if anschk(sf):
            flag = 1
        else:
            fc(sf)
            fc(sf)
        if anschk(sf):
            flag = 1
    fc(sf)
    if flag == 0:
        lc(sf)
        if anschk(sf):
            flag = 1
        else:
            lc(sf)
            lc(sf)
        if anschk(sf):
            flag = 1
    lc(sf)
    if flag == 0:
        rc(sf)
        if anschk(sf):
            flag = 1
        else:
            rc(sf)
            rc(sf)
        if anschk(sf):
            flag = 1
    rc(sf)
    if flag == 0:
        dc(sf)
        if anschk(sf):
            flag = 1
        else:
            dc(sf)
            dc(sf)
        if anschk(sf):
            flag = 1
    dc(sf)
    if flag == 0:
        bc(sf)
        if anschk(sf):
            flag = 1
        else:
            dc(sf)
            dc(sf)
        if anschk(sf):
            flag = 1
    if flag:
        print(1)
    else:
        print(0)


def uc(sf):
    sf[1][0], sf[1][1], sf[1][2], sf[1][3] = sf[1][2], sf[1][0], sf[1][3], sf[1][1]
    sf[0][2], sf[0][3],  sf[3][3], sf[3][1], sf[2][1], sf[2][0], sf[4][0], sf[4][2]\
        = sf[3][3], sf[3][1], sf[2][1], sf[2][0], sf[4][0], sf[4][2], sf[0][2], sf[0][3]
def fc(sf):
    sf[2][0], sf[2][1], sf[2][2], sf[2][3] = sf[2][2], sf[2][0], sf[2][3], sf[2][1]
    sf[1][2], sf[1][3], sf[3][2], sf[3][3], sf[5][2], sf[5][3], sf[4][2], sf[4][3]\
        = sf[3][2], sf[3][3], sf[5][2], sf[5][3], sf[4][2], sf[4][3], sf[1][2], sf[1][3]
def lc(sf):
    sf[3][0], sf[3][1], sf[3][2], sf[3][3] = sf[3][2], sf[3][0], sf[3][3], sf[3][1]
    sf[0][0], sf[0][2], sf[5][3], sf[5][1], sf[2][0], sf[2][2], sf[1][0], sf[1][2]\
        = sf[5][3], sf[5][1], sf[2][0], sf[2][2], sf[1][0], sf[1][2], sf[0][0], sf[0][2]
def rc(sf):
    sf[4][0], sf[4][1], sf[4][2], sf[4][3] = sf[4][2], sf[4][0], sf[4][3], sf[4][1]
    sf[5][0], sf[5][2], sf[0][3], sf[0][1], sf[1][3], sf[1][1], sf[2][1], sf[2][3] \
        = sf[0][3], sf[0][1], sf[1][3], sf[1][1], sf[2][1], sf[2][3], sf[5][2], sf[5][0]
def dc(sf):
    sf[5][0], sf[5][1], sf[5][2], sf[5][3] = sf[5][2], sf[5][0], sf[5][3], sf[5][1]
    sf[0][3], sf[0][1], sf[4][3], sf[4][1], sf[2][2], sf[2][3], sf[3][0], sf[3][2]\
        = sf[4][3], sf[4][1], sf[2][2], sf[2][3], sf[3][0], sf[3][2], sf[0][3], sf[0][1]
def bc(sf):
    sf[0][0], sf[0][1], sf[0][2], sf[0][3] = sf[0][2], sf[0][0], sf[0][3], sf[0][1]
    sf[5][0], sf[5][1], sf[3][0], sf[3][1], sf[1][0], sf[1][1], sf[4][0], sf[4][1]\
        = sf[3][0], sf[3][1], sf[1][0], sf[1][1], sf[4][0], sf[4][1], sf[5][0], sf[5][1]

def anschk(sf):
    for i in range(6):
        for j in range(3):
            if sf[i][j] != sf[i][j + 1]:
                return 0
    return 1


if __name__ == "__main__":
    main()
