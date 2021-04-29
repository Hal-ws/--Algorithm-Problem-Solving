import sys


def main():
    N = int(sys.stdin.readline())
    bList = []
    ansList = [0 for i in range(N)]
    colorSum = [0 for i in range(200001)] # i번 색깔별로 size 누적 합 기록
    maxColor = [[0, 0] for i in range(200001)] #i번 색깔별로 최대 size와 그 최대 size의 갯수 기록
    totalSum = [0 for i in range(2001)] # size i까지의 합(색깔 무관)
    for i in range(N):
        color, size = map(int, sys.stdin.readline().split())
        totalSum[size] += size
        bList.append([size, color, i])
    for i in range(1, 2001):
        totalSum[i] += totalSum[i - 1]
    bList.sort()
    for tmp in bList:
        size, color, bIdx = tmp[0], tmp[1], tmp[2]
        colorSum[color] += size
        if maxColor[color][0] == size:
            maxColor[color][1] += 1
        else:
            maxColor[color] = [size, 1]
        ansList[bIdx] = totalSum[size - 1] - colorSum[color] + (maxColor[color][0] * maxColor[color][1])
    for i in range(N):
        print(ansList[i])


if __name__ == '__main__':
    main()
