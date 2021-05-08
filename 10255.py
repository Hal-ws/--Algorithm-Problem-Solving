import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        xmin, ymin, xmax, ymax = map(int, sys.stdin.readline().split())
        box = [[xmin, ymin], [xmin, ymax], [xmax, ymin], [xmax, ymax]]
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        l1 = sorted([[x1, y1], [x2, y2]])
        if x1 == x2: # 수직인 직선일때
            print(chkVertical(l1, box))
        elif y1 == y2: # 수평인 직선일때
            print(chkHorizon(l1, box))
        else: # 사선인 직선일때
            chk = [0, 0, 0, 0]
            pCross = 0
            chk[0] = crossChk(l1, [box[0], box[1]])
            chk[1] = crossChk(l1, [box[0], box[2]])
            chk[2] = crossChk(l1, [box[1], box[3]])
            chk[3] = crossChk(l1, [box[2], box[3]])
            if chk[0] == chk[1] == 1:
                pCross += pointChk(l1, [xmin, ymin])
            if chk[0] == chk[2] == 1:
                pCross += pointChk(l1, [xmin, ymax])
            if chk[3] == chk[1] == 1:
                pCross += pointChk(l1, [xmax, ymin])
            if chk[3] == chk[2] == 1:
                pCross += pointChk(l1, [xmax, ymax])
            print(sum(chk) - pCross)


def pointChk(l1, p):
    a, b = p[0], p[1]
    x1, y1, x2, y2 = l1[0][0], l1[0][1], l1[1][0], l1[1][1]
    if x1 <= a <= x2:
        if (x2 - x1) * b == (y2 - y1) * (a - x1) + y1 * (x2 - x1):
            return 1
        return 0
    else:
        return 0


def chkVertical(l1, box): #
    x, y1, y2 = l1[0][0], l1[0][1], l1[1][1]
    xmin, ymin, xmax, ymax = box[0][0], box[0][1], box[3][0], box[3][1]
    # 0이 되는 경우
    if x < xmin or x > xmax:
        return 0
    if y2 < ymin or y1 > ymax:
        return 0
    # 양쪽 두 변
    if x == xmin or x == xmax:
        if y2 == ymin or y1 == ymax:
            return 1
        else:
            return 4
    # 사이
    if y2 > ymax:
        if ymin < y1 <= ymax:
            return 1
        if y1 <= ymin:
            return 2
    if y2 == ymax:
        if ymin < y1:
            return 1
        if ymin >= y1:
            return 2
    if ymin < y2 < ymax:
        if y1 > ymin:
            return 0
        if y1 <= ymin:
            return 1
    if ymin == y2:
        return 1


def chkHorizon(l1, box): #
    x1, y, x2 = l1[0][0], l1[0][1], l1[1][0]
    xmin, ymin, xmax, ymax = box[0][0], box[0][1], box[3][0], box[3][1]
    # 0이 되는경우
    if y < ymin or y > ymax:
        return 0
    if x1 > xmax or x2 < xmin:
        return 0
    # 위아래 두 변
    if y == ymin or y == ymax:
        if xmax == x1 or xmin == x2:
            return 1
        else:
            return 4
    # 사이
    if x2 > xmax:
        if xmin < x1 <= xmax:
            return 1
        if x1 <= xmin:
            return 2
    if x2 == xmax:
        if xmin < x1:
            return 1
        if x1 <= xmin:
            return 2
    if xmin < x2 < xmax:
        if xmin < x1:
            return 0
        if x1 <= xmin:
            return 1
    if x2 == xmin:
        return 1

def crossChk(l1, l2): # l1은 수직 아님. l2는 수직 아니면 수평
    x1, y1, x2, y2 = l1[0][0], l1[0][1], l1[1][0], l1[1][1]
    x3, y3, x4, y4 = l2[0][0], l2[0][1], l2[1][0], l2[1][1]
    xd1, xd2, yd1, yd2 = (x2 - x1), (x4 - x3), (y2 - y1), (y4 - y3)
    if x1 == x2 and x3 != x4:
        if x3 <= x1 <= x4:
            if y1 <= yd2 / xd2 * (x1 - x3) + y3 <= y2:
                ans = 1
            else:
                ans = 0
        else:
            ans = 0
    elif x1 != x2 and x3 == x4:
        if x1 <= x3 <= x2:
            if y3 <= yd1 / xd1 * (x3 - x1) + y1 <= y4:
                ans = 1
            else:
                ans = 0
        else:
            ans = 0
    elif x1 == x2 and x3 == x4:
        if x1 != x3:
            ans = 0
        else:
            if y1 <= y4 <= y2 or y3 <= y2 <= y4:
                ans = 1
            else:
                ans = 0
    else:
        if yd1 * xd2 == yd2 * xd1: # 기울기 같음
            if yd1 * (-x1) * xd2 + y1 * xd1 * xd2 == yd2 * (-x3) * xd1 + y3 * xd1 * xd2: # 같은 y절편
                if x1 <= x3 <= x2 or x1 <= x4 <= x2: # 범위 겹침
                    ans = 1
                else: #범위 안겹침
                    ans = 0
            else: # y절편값 다름
                ans = 0
        else: # 기울기 다름
            if x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4: #범위 겹침
                p = yd1 * xd2 * x1 - yd2 * xd1 * x3 + xd1 * xd2 * (y3 - y1)
                flag1, flag2 = 0, 0
                if x1 * (yd1 * xd2 - yd2 * xd1) <= p <= x2 * (yd1 * xd2 - yd2 * xd1) or x2 * (yd1 * xd2 - yd2 * xd1) <= p <= x1 * (yd1 * xd2 - yd2 * xd1):
                    flag1 = 1
                    if x3 * (yd1 * xd2 - yd2 * xd1) <= p <= x4 * (yd1 * xd2 - yd2 * xd1) or x4 * (yd1 * xd2 - yd2 * xd1) <= p <= x3 * (yd1 * xd2 - yd2 * xd1):
                        flag2 = 1
                if flag1 and flag2:
                    ans = 1
                else:
                    ans = 0
            else:
                ans = 0
    return ans


if __name__ == '__main__':
    main()
