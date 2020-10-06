import sys

n = int(sys.stdin.readline())
stairs = []
for i in range(n):
    stairs.append(int(sys.stdin.readline()))
if n < 2:
    maxVal = [[stairs[0], 0]]
else:
    maxVal = [[stairs[0], 0, 1], [stairs[0] + stairs[1], stairs[1], 2]]
for i in range(2, n):
    if maxVal[i - 1][2] == 2:
        maxVal.append([maxVal[i - 1][1] + stairs[i], max(maxVal[i - 2][0], maxVal[i - 2][1]) + stairs[i], None])
        if maxVal[i][0] > maxVal[i][1]:
            maxVal[i][2] = 2
        else:
            maxVal[i][2] = 1
    else:
        maxVal.append([max(maxVal[i - 1][0], maxVal[i - 1][1]) + stairs[i], max(maxVal[i - 2][0], maxVal[i - 2][1]) + stairs[i], None])
        if maxVal[i][0] > maxVal[i][1]:
            maxVal[i][2] = 2
        else:
            maxVal[i][2] = 1
print(max(maxVal[i][:2]))
