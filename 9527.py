def main():
    A, B = map(int, input().split())
    cntList = [pow(2, i - 1) for i in range(55)] # 최고자리에 있는 1의 갯수 더해줌
    cntList[0] = 0
    for digit in range(1, 55):
        addCnt = 0
        for i in range(1, digit):
            addCnt += (getC(digit - 1, i) * i)
        cntList[digit] += addCnt
    answer = get1Cnt(B, cntList) - get1Cnt(A - 1, cntList)
    print(answer)


def get1Cnt(n, cntList):
    i = 1
    cnt1 = 0
    while n > 0:
        while 1:
            if n == pow(2, i) - 1:
                cnt1 += cntList[i]
                n = 0
                break
            elif pow(2, i) - 1 > n:
                lastDigit = i - 1 # 커지지 않은 최대의 digit
                minusVal = pow(2, lastDigit)
                cnt1 += (n - minusVal + 1)
                n -= minusVal
                i = 1
                break
            cnt1 += cntList[i]
            i += 1
    return cnt1


def getC(n, r):
    return getFac(n) // (getFac(r) * getFac(n - r))


def getFac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    main()
