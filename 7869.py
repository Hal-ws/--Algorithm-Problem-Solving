import sys
from math import sqrt, acos


def main():
    x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())
    dSquare = pow(x2 - x1, 2) + pow(y2 - y1, 2)
    d = sqrt(dSquare)
    pi = 3.14159265358979323846264338
    if dSquare >= pow(r1 + r2, 2): # 한 원이 다른 원의 완전한 외부에 있음
        print('0.000')
        return 0
    else:
        if dSquare < pow(abs(r1 - r2), 2) or dSquare == 0: # 내부에 있거나, 중심이 일치함
            answer = pow(min(r1, r2), 2) * pi
        else: # 두 원이 두 점에서 만남
            x1, x2 = 0, d #
            crossX = (pow(r1, 2) - pow(r2, 2) + dSquare) / (2 * d)
            crossY = sqrt(pow(r1, 2) - pow(crossX, 2))
            cos1 = (2 * pow(r1, 2) - 4 * pow(crossY, 2)) / (2 * pow(r1, 2))
            cos2 = (2 * pow(r2, 2) - 4 * pow(crossY, 2)) / (2 * pow(r2, 2))
            if cos1 < -1:
                cos1 = -1
            if cos1 > 1:
                cos1 = 1
            if cos2 < -1:
                cos2 = -1
            if cos2 > 1:
                cos2 = 1
            theta1, theta2 = acos(cos1), acos(cos2)
            area1 = (pow(r1, 2) * theta1 / 2) - (abs(crossX) * crossY)
            area2 = (pow(r2, 2) * theta2 / 2) - (abs(x2 - crossX) * crossY)
            if crossX < 0:
                area1 = pi * pow(r1, 2) - area1
            if crossX > d:
                area2 = pi * pow(r2, 2) - area2
            answer = area1 + area2
        print('%.3f' %answer)


if __name__ == '__main__':
    main()
