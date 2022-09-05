import sys
from collections import deque


def main():
    N, P = map(int, sys.stdin.readline().split())
    answer = 0
    guitar = [deque() for i in range(6)]
    for i in range(6):
        guitar[i].append(0)
    for _ in range(N):
        stringNumber, fretNumber = map(int, sys.stdin.readline().split())
        answer += playingGuitar(guitar, stringNumber, fretNumber)
    print(answer)


def playingGuitar(guitar, stringNumber, fretNumber):
    count = 0
    stringNumber -= 1
    while 1:
        if guitar[stringNumber][-1] == fretNumber:
            break
        if guitar[stringNumber][-1] < fretNumber:
            guitar[stringNumber].append(fretNumber)
            count += 1
            break
        if guitar[stringNumber][-1] > fretNumber:
            guitar[stringNumber].pop()
            count += 1
    return count


if __name__ == "__main__":
    main()
