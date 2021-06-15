import sys


def main():
    N = int(sys.stdin.readline())
    nList = []
    answer = 0
    for i in range(N):
        num = int(sys.stdin.readline())
        nList.append([num, i])
    nList.sort()
    for nIdx in range(N):
        pIdx = nList[nIdx][1]
        if pIdx - nIdx> answer:
            answer = pIdx - nIdx
    print(answer + 1)


if __name__ == '__main__':
    main()
