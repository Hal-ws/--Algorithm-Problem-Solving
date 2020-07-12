def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    l1 = sorted([[x1, y1], [x2, y2]])
    l2 = sorted([[x3, y3], [x4, y4]])
    range = [None, None]
    if l1[1][0] < l2[0][0]:
        print(0)
        return 0
    elif l2[0][0] <= l1[1][0] <= l2[1][0]:
        range = [max(l2[0][0], l1[0][0]), l1[1][0]]
    else:
        if l1[0][0] > l2[1][0]:
            print(0)
            return 0
        else:
            range = [max(l1[0][0], l2[0][0]), l2[1][0]]
    flag = 1
    if l1[0][0] != l1[1][0] and l2[0][0] != l2[1][0]:
        d1 = (l1[1][1] - l1[0][1]) / (l1[1][0] - l1[0][0]) * (range[0] - l1[0][0]) + l1[0][1]
        d2 = (l2[1][1] - l2[0][1]) / (l2[1][0] - l2[0][0]) * (range[0] - l2[0][0]) + l2[0][1]
        d3 = (l1[1][1] - l1[0][1]) / (l1[1][0] - l1[0][0]) * (range[1] - l1[0][0]) + l1[0][1]
        d4 = (l2[1][1] - l2[0][1]) / (l2[1][0] - l2[0][0]) * (range[1] - l2[0][0]) + l2[0][1]
    else:
        flag = 0
        if l1[0][0] == l1[1][0] and l2[0][0] != l2[1][0]:
            case = 0
        elif l1[0][0] != l1[1][0] and l2[0][0] == l2[1][0]:
            case = 1
        else:
            case = 2
    if flag:
        if (d1 - d2) * (d3 - d4) <= 0:
            print(1)
        else:
            print(0)
        return 0
    elif case == 0:
        if l1[0][1] <= (l2[1][1] - l2[0][1]) / (l2[1][0] - l2[0][0]) * (l1[0][0] - l2[0][0]) + l2[0][1] <= l1[1][1]:
            print(1)
        else:
            print(0)
    elif case == 1:
        if l2[0][1] <= (l1[1][1] - l1[0][1]) / (l1[1][0] - l1[0][0]) * (l2[0][0] - l1[0][0]) + l1[0][1] <= l2[1][1]:
            print(1)
        else:
            print(0)
    else:
        if l2[0][1] <= l1[1][1] <= l2[1][1] or l1[0][1] <= l2[1][1] <= l1[1][1]:
            print(1)
        else:
            print(0)
    return 0

if __name__ == "__main__":
    main()
