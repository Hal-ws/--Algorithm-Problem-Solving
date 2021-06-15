import sys
from math import sqrt


def main():
    Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, sys.stdin.readline().split())
    d1, d2 = getDis([Ax, Ay, Az], [Cx, Cy, Cz]), getDis([Bx, By, Bz], [Cx, Cy, Cz])
    if d1 >= d2:
        farP = [Ax, Ay, Az]
        nearP = [Bx, By, Bz]
    else:
        nearP = [Ax, Ay, Az]
        farP = [Bx, By, Bz]
    while 1:
        d1, d2 = getDis(nearP, [Cx, Cy, Cz]), getDis(farP, [Cx, Cy, Cz])
        if d1 >= d2:
            farP, nearP = [nearP[0], nearP[1], nearP[2]], [farP[0], farP[1], farP[2]]
        else:
            farP, nearP = [farP[0], farP[1], farP[2]], [nearP[0], nearP[1], nearP[2]]
        midP = [(nearP[0] + farP[0]) / 2, (nearP[1] + farP[1]) / 2, (nearP[2] + farP[2]) / 2]
        d3 = getDis(midP, [Cx, Cy, Cz])
        if abs(d3 - d1) < pow(10, -6) and abs(d3 - d2) < pow(10, -6):
            if d3 < pow(10, -6):
                print(0)
            else:
                print(d3)
            break
        farP = [midP[0], midP[1], midP[2]]


def getDis(p1, p2):
    return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2) + pow(p1[2] - p2[2], 2))


if __name__ == '__main__':
    main()
