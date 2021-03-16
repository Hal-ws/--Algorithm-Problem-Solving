import sys


def main():
    N = int(sys.stdin.readline())
    matrix = []
    dp = [[0 for j in range(N)] for i in range(N)]
    size = [[[0, 0] for j in range(N)] for i in range(N)] # i부터 j까지 최소로 합쳤을때의 크기 저장
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    for l in range(2, N + 1): # 길이가 2부터 N까지인것 차곡차곡
        for i in range(0, N + 1 - l): # 시작값
            j = i + l - 1
            if j == i + 1:
                dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
                size[i][j] = [matrix[i][0], matrix[j][1]]
            else:
                # i~j - 1 와 j 곱함
                val1 = size[i][j - 1][0] * size[i][j - 1][1] * matrix[j][1]
                size1 = [size[i][j - 1][0], matrix[j][1]]
                # i 와 i + 1 ~ j 곱함
                val2 = matrix[i][0] * matrix[i][1] * size[i + 1][j][1]
                size2 = [matrix[i][0], size[i + 1][j][1]]
                if val1 < val2:
                    dp[i][j] = val1
                    size[i][j] = size1
                else:
                    dp[i][j] = val2
                    size[i][j] = size2
    for i in range(N):
        print(dp[i])
    print('----------------')
    for i in range(N):
        print(size[i])
    print(dp[0][N - 1])

if __name__ == '__main__':
    main()
