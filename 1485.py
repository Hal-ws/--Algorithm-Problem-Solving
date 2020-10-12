import sys

def checkangle(p1, p3, p4):
    if (p3[0] - p1[0]) * (p4[0] - p1[0]) + (p3[1] - p1[1]) * (p4[1] - p1[1]) == 0:
        return True
    return False

T = int(sys.stdin.readline())
for i in range(T):
    p = []
    flag = 0
    for j in range(4):
        p.append(list(map(int, sys.stdin.readline().split())))
    length = [pow(p[1][0] - p[0][0], 2) + pow(p[1][1] - p[0][1], 2), pow(p[2][0] - p[0][0], 2) + pow(p[2][1] - p[0][1], 2), pow(p[3][0] - p[0][0], 2) + pow(p[3][1] - p[0][1], 2)]
    if length[0] == length[1] + length[2] and length[1] == length[2]:
        if checkangle(p[0], p[2], p[3]) and checkangle(p[2], p[0], p[1]):
            flag = 1
    if length[1] == length[0] + length[2] and length[0] == length[2]:
        if checkangle(p[0], p[1], p[3]) and checkangle(p[1], p[0], p[2]):
            flag = 1
    if length[2] == length[0] + length[1] and length[0] == length[1]:
        if checkangle(p[0], p[1], p[2]) and checkangle(p[1], p[0], p[3]):
            flag = 1
    if flag:
        print(1)
    else:
        print(0)
