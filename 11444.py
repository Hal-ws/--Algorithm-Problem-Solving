def main():
    n = int(input())
    if n == 0 or n == 1:
        print(n)
        return
    tmp = getAns([[1, 1], [1, 0]], n - 1)
    print(tmp[0][0])


def getAns(a, b):
    if b == 1:
        return a
    tmp = getAns(a, b // 2)
    if b % 2 == 0:
        return multi(tmp, tmp)
    else:
        tmp2 = multi(tmp, tmp)
        return multi(tmp2, [[1, 1], [1, 0]])


def multi(m1, m2):
    a = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % 1000000007
    b = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % 1000000007
    c = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % 1000000007
    d = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % 1000000007
    return [[a, b], [c, d]]


if __name__ == '__main__':
    main()
