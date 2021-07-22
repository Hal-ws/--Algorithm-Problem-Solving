import sys


def main():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    l1 = sorted([[x1, y1], [x2, y2]])
    l2 = sorted([[x3, y3], [x4, y4]])
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
                if x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4: # 범위 겹침
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
    print(ans)


if __name__ == '__main__':
    main()
