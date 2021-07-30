import sys
from math import sqrt


def main():
    a, b = map(int, sys.stdin.readline().split())
    pList = makePalindrome()
    for i in range(10):
        pList[i].sort()
    for i in range(10):
        for j in range(len(pList[i])):
            num = pList[i][j]
            if a <= num <= b and chkPrime(num):
                print(num)
            if num > b:
                break
    print(-1)


def chkPrime(num):
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return 0
        i += 1
    return 1


def makePalindrome():
    pList = [[] for i in range(10)] # 팰린드롬의 수를 저장
    pList[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pList[2] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    for i in range(3, 9): #길이가 3부터 8까지 구함
        if i % 2: #길이가 홀수인걸 구함
            for num in pList[i - 1]: # 길이가 i - 1인 num들을 가지고 와서 구해줌
                nStr = str(num)
                for newNum in range(10): # 0부터 10까지의 값을 사이에 끼워줌
                    pList[i].append(int(nStr[:(i - 1) // 2] + str(newNum) + nStr[(i - 1) // 2:]))
        else: # 길이가 짝수인걸 구함
            for num in pList[i - 1]:
                nStr = str(num)
                pList[i].append(int(nStr[:(i - 1) // 2] + nStr[(i - 1) // 2] * 2 +nStr[(i - 1) // 2 + 1:]))
    return pList


if __name__ == '__main__':
    main()
