from math import gcd


def main():
    N = int(input())
    upNum = [0] * N
    downNum = [0] * N
    lcd = 1
    nums = list(map(int, input().split()))
    for i in range(N):
        downNum[i] = nums[i]
        upNum[i] = 1
        lcd = nums[i] * lcd // gcd(nums[i], lcd)
    for i in range(N):
        upNum[i] = lcd // downNum[i]
        downNum[i] = lcd
    upVal = sum(upNum)
    downVal = lcd
    print('%s/%s' %(downVal // gcd(upVal, downVal), upVal // gcd(upVal, downVal)))


if __name__ == "__main__":
    main()
