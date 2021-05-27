import sys


def main():
    t = 1
    while 1:
        tList = list(map(int, sys.stdin.readline().split()))
        layer = tList[0]
        ans = -1 * (400 * 799 * 1000) - 1
        if layer == 0:
            break
        tList = tList[1:]
        triangle = [[0 for j in range(2 * layer - 1)] for i in range(layer)]
        sTriangle = [[0 for j in range(2 * layer - 1)] for i in range(layer)]
        for i in range(layer):
            start = pow(i, 2)
            for j in range(start, start + 2 * i + 1):
                triangle[i][j - start] = tList[j]
                if j == start:
                    sTriangle[i][j - start] = tList[j]
                else:
                    sTriangle[i][j - start] = tList[j] + sTriangle[i][j - start - 1]
        # 정방향
        for i in range(layer):
            for j in range(0, 2 * i + 1, 2):
                tmpVal = 0
                for size in range(1, layer - i + 1):
                    if j == 0:
                        tmpVal += sTriangle[i + size - 1][(size - 1) * 2]
                    else:
                        tmpVal += (sTriangle[i + size - 1][j + (size - 1) * 2] - sTriangle[i + size - 1][j - 1])
                    if tmpVal > ans:
                        ans = tmpVal
        # 역방향
        for i in range(layer -1, 2, -1): # i 가 3보다는 같거나 커야 역방향 삼각형이 있을 수 있음
            for j in range(3, 2 * i + 1, 2):
                tmpVal = triangle[i][j]
                if i % 2 == 0:
                    maxSize = i // 2
                else:
                    maxSize = (i // 2) + 1
                for size in range(2, maxSize + 1):
                    chkY = i - size + 1
                    if j > chkY * 2 or j - 2 * (size - 1) < 1:
                        break
                    tmpVal += (sTriangle[i - size + 1][j] - sTriangle[i - size + 1][j - (size * 2 - 1)])
                    if tmpVal > ans:
                        ans = tmpVal
        print('%s. %s' %(t, ans))
        t += 1


if __name__ == '__main__':
    main()
