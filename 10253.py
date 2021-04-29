import sys
from math import gcd


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        while 1: #
            if b % a == 0: # 나누어 떨어지면
                print(b)
                break
            xn = b // a + 1
            a, b = minus(xn, a, b) # a / b 에서 1 / xn


def minus(xn, a, b): # a / b 에서 1 / xn를 뺀 분수를 return(뺀 값의 분자가 a, 분모가 b)
    lcd = (b * xn) // gcd(xn, b)
    a = (a * (lcd // b) - lcd // xn)
    b = lcd
    val = gcd(a, b) # a, b 약분해줌
    a = a // val
    b = b // val
    return a, b


if __name__ == '__main__':
    main()
