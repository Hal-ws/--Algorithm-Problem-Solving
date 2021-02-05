from math import sqrt


def main():
    N = int(input())
    if pow(int(sqrt(N)), 2) == N:
        print(1)
        return
    maxN = int(sqrt(N))
    for i in range(maxN, 1, -1):
        for j in range(i - 1, 0, -1):
            if pow(i, 2) + pow(j, 2) == N:
                print(2)
                return
    for i in range(maxN, 2, -1):
        left = N - pow(i, 2)
        max2 = int(sqrt(left))
        for j in range(max2, 1, -1):
            left2 = left - pow(j, 2)
            max3 = int(sqrt(left))
            for k in range(max3, 0, -1):
                left3 = left2 - pow(k, 2)
                if left3 == 0:
                    print(3)
                    return
    print(4)
    return


if __name__ == '__main__':
    main()
