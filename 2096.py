import sys


def main():
    N = int(sys.stdin.readline())
    tmp = list(map(int, sys.stdin.readline().split()))
    dpMax = [[0, 0, 0] for i in range(2)]
    dpMin = [[0, 0, 0] for i in range(2)]
    dpMax[0][0], dpMax[0][1], dpMax[0][2] = tmp[0], tmp[1], tmp[2]
    dpMin[0][0], dpMin[0][1], dpMin[0][2] = tmp[0], tmp[1], tmp[2]
    if N == 1:
        print('%s %s' %(max(tmp), min(tmp)))
        return
    for i in range(1, N):
        tmp = list(map(int, sys.stdin.readline().split()))
        dpMax[1][0] = max(dpMax[0][0], dpMax[0][1]) + tmp[0]
        dpMax[1][1] = max(dpMax[0][0], dpMax[0][1], dpMax[0][2]) + tmp[1]
        dpMax[1][2] = max(dpMax[0][1], dpMax[0][2]) + tmp[2]
        dpMin[1][0] = min(dpMin[0][0], dpMin[0][1]) + tmp[0]
        dpMin[1][1] = min(dpMin[0][0], dpMin[0][1], dpMin[0][2]) + tmp[1]
        dpMin[1][2] = min(dpMin[0][1], dpMin[0][2]) + tmp[2]
        if i != N - 1:
            dpMax[0] = [dpMax[1][0], dpMax[1][1], dpMax[1][2]]
            dpMin[0] = [dpMin[1][0], dpMin[1][1], dpMin[1][2]]
    print('%s %s' %(max(dpMax[1]), min(dpMin[1])))


if __name__ == '__main__':
    main()
