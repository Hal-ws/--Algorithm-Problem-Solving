import sys


def main():
    N = int(sys.stdin.readline())
    towers = list(map(int, sys.stdin.readline().split()))
    stack = [[100000001, 0]] # 무조건 만남
    ansList = [0] * N
    for i in range(N):
        h = towers[i]
        while 1:
            tmp = stack.pop()
            cmpH, idx = tmp[0], tmp[1]
            if cmpH >= h:
                ansList[i] = idx
                stack.append(tmp)
                break
        stack.append([h, i + 1])
    for num in ansList:
        print(num, end=' ')
    return 0


if __name__ == '__main__':
    main()
