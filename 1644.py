import math

def main():
    N = int(input())
    cnt = 0
    primeList = [0] + getprimelist(N)
    length = len(primeList)
    maxVals = [primeList[0]]
    for i in range(1, length):
        maxVals.append(primeList[i] + maxVals[i - 1])
    s = 0
    e = 1
    while e < length:
        if maxVals[e] - maxVals[s] == N:
            cnt += 1
            e += 1
        elif maxVals[e] - maxVals[s] < N:
            e += 1
        else:
            s += 1
    print(cnt)

def getprimelist(number):
    std = int(math.sqrt(number))
    numList = [None] * 2 + [True] * (number - 1)
    primeList = []
    for i in range(2, std + 1):
        if numList[i] == False:
            continue
        j = i + i
        while j < number + 1:
            numList[j] = False
            j += i
    for i in range(2, number + 1):
        if numList[i]:
            primeList.append(i)
    return primeList

if __name__ == "__main__":
    main()
