import sys

n = int(sys.stdin.readline())
triangle = []
for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))
memo = [[triangle[0][0]]]
for i in range(1, n):
    temp = [0] * (i + 1)
    for j in range(i + 1):
        if j == 0:
            temp[0] = memo[i - 1][0] + triangle[i][j]
        elif j == i:
            temp[j] = memo[i - 1][i - 1] + triangle[i][j]
        else:
            temp[j] = max(memo[i - 1][j - 1], memo[i - 1][j]) + triangle[i][j]
    memo.append(temp)
print(max(memo[n - 1]))
