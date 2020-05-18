N = int(input())

wide = 4 * N - 3
if N == 1:
    height = 1
    endPoint = [0, 0]
else:
    height = 4 * N - 1
    endPoint = [2 * N, 2 * (N - 1)]
plate = [[' '] * wide for i in range(height)]

i = 0
j = wide - 1
leftEnd = 0
rightEnd = wide - 1
topEnd = 2
bottomEnd = height - 1
direction = 'l'

while i != endPoint[0] or j != endPoint[1]:
    plate[i][j] = '*'
    if direction == 'l':
        if j > leftEnd:
            j -= 1
        else:
            direction = 'd'
            leftEnd += 2
    if direction == 'd':
        if i < bottomEnd:
            i += 1
        else:
            direction = 'r'
            bottomEnd -= 2
    if direction == 'r':
        if j < rightEnd:
            j += 1
        else:
            direction = 'u'
            rightEnd -= 2
    if direction == 'u':
        if i > topEnd:
            i -= 1
        else:
            direction = 'l'
            topEnd += 2


plate[endPoint[0]][endPoint[1]] = '*'
for i in range(height):
    if i == 1:
        print('*', end = '')
    for j in range(wide):
        if i != 1:
            print(plate[i][j], end ='')
    print()
