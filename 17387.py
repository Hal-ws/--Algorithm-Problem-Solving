def main():
    x1, y1, x2, y2 = map(float, input().split())
    x3, y3, x4, y4 = map(float, input().split())
    l1 = sorted([[x1, y1], [x2, y2]])
    l2 = sorted([[x3, y3], [x4, y4]])
    if x1 != x2 and x3 != x4:
        m1, m2 = (y2 - y1) / (x2 - x1), (y4 - y3) / (x4 - x3)
        if m1 == m2:
            print(parallel(l1, l2, m1))
        else:
            print(crossing(l1, l2, m1, m2))
    elif x1 == x2 and x3 != x4:
        m2 = (y4 - y3) / (x4 - x3)
        y = m2(x1 - x3) + m2 * (-1) * l2[0][0] + l2[0][1]
        if l1[0][1] <= y <= l1[1][1] and l2[0][1] <= y <= l2[1][1]:
            print(1)
        else:
            print(0)
    elif x1 != x2 and x3 == x4:
        m1 = (y2 - y1) / (x2 - x1)
        y = m1(x3 - x1) + m1 * (-1) * l1[0][0] + l1[0][1]
        if l2[0][1] <= y <= l2[1][1] and l1[0][1] <= y <= l1[1][1]:
            print(1)
        else:
            print(0)
    else:
        if l1[0][1] <= l2[0][1] <= l1[1][1] or l1[0][1] <= l2[1][1] <= l1[1][1]:
            print(1)
        else:
            print(0)


def parallel(l1, l2, m1):
    y1, y2 = m1 * (0 - l1[0][0]) + l1[0][1], m1 * (0 - l2[0][0]) + l2[0][1]
    if y1 != y2:
        return 0
    else:
        if l1[0][0] <= l2[0][0] <= l1[1][0] or l1[0][0] <= l2[1][0] <= l1[0][0]:
            return 1
        else:
            return 0


def crossing(l1, l2, m1, m2):
    a1 = m1 * (-1) * l1[0][0] + l1[0][1]
    a2 = m2 * (-1) * l2[0][0] + l2[0][1]
    crossp = (a1 - a2) / (m2 - m1)
    if l1[0][0] <= crossp <= l1[1][0]:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
