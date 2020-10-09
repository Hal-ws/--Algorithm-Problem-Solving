import sys

N = int(sys.stdin.readline())
fileNames = []
for i in range(N):
    fileNames.append(sys.stdin.readline())

ans = ''
for i in range(len(fileNames[0])):
    flag = 0
    j = 1
    while j < len(fileNames):
        if fileNames[0][i] != fileNames[j][i]:
            ans += '?'
            break
        j += 1
    if j == len(fileNames):
        ans += str(fileNames[j - 1][i])
print(ans)
