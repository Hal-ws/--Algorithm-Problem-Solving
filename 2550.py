import sys


def main():
    N = int(sys.stdin.readline())
    sList = list(map(int, sys.stdin.readline().split()))
    tList = list(map(int, sys.stdin.readline().split()))
    wires = [0 for i in range(N)]
    idxBook = {}
    for i in range(N):
        target = tList[i]
        idxBook[target] = i
    for i in range(N):
        start = sList[i]
        wires[i] = idxBook[start]
    print(wires)


if __name__ == "__main__":
    main()
