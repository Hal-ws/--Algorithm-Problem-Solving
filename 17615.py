N = int(input())

balls = input()

def getseperated(balls):
    group = [[balls[0], 1]]
    for i in range(1, len(balls)):
        if balls[i] != balls[i - 1]:
            group.append([balls[i], 1])
        else:
            group[len(group) - 1][1] += 1
    return group

seperated = getseperated(balls)
if len(seperated) <= 2:
    print(0)
else:
    case1 = 0 ## red를 옮기는경우
    for i in range(len(seperated)):
        if seperated[i][0] == 'R':
            case1 += seperated[i][1]
    if seperated[0][0] == 'R' and seperated[len(seperated) - 1][0] == 'R':
        if seperated[0][1] > seperated[len(seperated) - 1][1]:
            case1 -= seperated[0][1]
        else:
            case1 -= seperated[len(seperated) - 1][1]
    elif seperated[0][0] == 'R':
        case1 -= seperated[0][1]
    elif seperated[len(seperated) - 1][0] == 'R':
        case1 -= seperated[len(seperated) - 1][1]
    case2 = 0 ## blue를 옮기는경우
    for i in range(len(seperated)):
        if seperated[i][0] == 'B':
            case2 += seperated[i][1]
    if seperated[0][0] == 'B' and seperated[len(seperated) - 1][0] == 'B':
        if seperated[0][1] > seperated[len(seperated) - 1][1]:
            case2 -= seperated[0][1]
        else:
            case2 -= seperated[len(seperated) - 1][1]
    elif seperated[0][0] == 'B':
        case2 -= seperated[0][1]
    elif seperated[len(seperated) - 1][0] == 'B':
        case2 -= seperated[len(seperated) - 1][1]
    if case1 < case2:
        print(case1)
    else:
        print(case2)
