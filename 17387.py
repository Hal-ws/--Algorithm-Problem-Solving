import sys


def main():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    l1 = sorted([[x1, y1], [x2, y2]])
    l2 = sorted([[x3, y3], [x4, y4]])
    x1, y1, x2, y2 = l1[0][0], l1[0][1], l1[1][0], l1[1][1]
    x3, y3, x4, y4 = l2[0][0], l2[0][1], l2[1][0], l2[1][1]
    if x1 == x2 and x3 != x4:
        if x1 < x3 or x1 > x4:
            ans = 0
        else:
            if y1 <= (y4 - y3) / (x4 - x3) * (x1 - x3) + y3 <= y2:
                ans = 1
            else:
                ans = 0
    elif x1 != x2 and x3 == x4:
        if x3 < x1 or x2 < x3:
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
        if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1): # 기울기 같음
            if
    print(ans)


if __name__ == '__main__':
    main()
