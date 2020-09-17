import sys


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        a, b = map(int, sys.stdin.readline().split())
        print(get2017reward(a) + get2018reward(b))


def get2017reward(a):
    if a > 21 or a == 0:
        return 0
    if a == 1:
        return 5000000
    elif 2 <= a < 4:
        return 3000000
    elif 4 <= a < 7:
        return 2000000
    elif 7 <= a < 11:
        return 500000
    elif 11 <= a < 16:
        return 300000
    else:
        return 100000


def get2018reward(b):
    if b > 31 or b == 0:
        return 0
    if b == 1:
        return 5120000
    elif 2 <= b < 4:
        return 2560000
    elif 4 <= b < 8:
        return 1280000
    elif 8 <= b < 16:
        return 640000
    else:
        return 320000


if __name__ == "__main__":
    main()
