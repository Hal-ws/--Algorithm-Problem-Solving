import sys
from math import sqrt


def main():
    a, b, c = map(float, sys.stdin.readline().split())
    left, right = 0, min(a, b)
    flag = 0
    while left < right:
        d = (left + right) / 2
        aVal = sqrt(pow(a, 2) - pow(d, 2))
        bVal = sqrt(pow(b, 2) - pow(d, 2))
        h = aVal / (1 + aVal / bVal)
        if abs(h - c) < 0.0000001:
            print("{:.3f}".format(d))
            flag = 1
            break
        if h > c:
            left = d + 0.000001
        else:
            right = d - 0.000001
    if flag == 0:
        print("{:.3f}".format(d))


if __name__ == '__main__':
    main()
