import sys


def main():
    n = int(sys.stdin.readline())
    schedule = []
    ansList = [0] * 10001
    for i in range(n):
        p, d = map(int, sys.stdin.readline().split())
        schedule.append([d, p])
    schedule.sort()
    for i in range(n):
        p, d = schedule[i][1], schedule[i][0]
        minV, dIdx = 10001, -1
        for j in range(1, d + 1):
            if ansList[j] == 0: #빈칸 찾았을때
                dIdx = j
                minV = 0
                break
            else:
                if ansList[j] < minV:
                    minV = ansList[j]
                    dIdx = j
        if dIdx != -1: #dIdx 를 찾았을때
            if minV < p:
                ansList[dIdx] = p
    print(sum(ansList))


if __name__ == '__main__':
    main()
