import sys
from collections import deque
from itertools import combinations


def main():
    board = ['000000000000']
    for _ in range(10):
        board.append('0' + sys.stdin.readline()[:10] + '0')
    endPoints = [[], [], [], []]
    sIdx = [[0, 12, 1, 0, 12, 1], [11, -1, -1, 0, 12, 1], [0, 12, 1, 0, 12, 1], [0, 12, 1, 11, -1, -1]]
    board.append('000000000000')
    edges = []
    for i in range(4):
        sy, ey, d1 = sIdx[i][0], sIdx[i][1], sIdx[i][2]
        sx, ex, d2 = sIdx[i][3], sIdx[i][4], sIdx[i][5]
        if i < 2:
            for y in range(sy, ey, d1):
                flag = 0
                for x in range(sx, ex, d2):
                    if board[y][x] == '1':
                        endPoints[i].append([y, x])
                        flag = 1
                if flag:
                    break
        else:
            for x in range(sx, ex, d2):
                flag = 0
                for y in range(sy, ey, d1):
                    if board[y][x] == '1':
                        endPoints[i].append([y, x])
                        flag = 1
                if flag:
                    break
    for i in range(4):
        if endPoints[i][0] not in edges:
            edges.append(endPoints[i][0])
        if endPoints[i][-1] not in edges:
            edges.append(endPoints[i][-1])
    edges.sort()
    if len(edges) != 3:
        print(0)
        return
    y1, x1, y2, x2, y3, x3 = edges[0][0], edges[0][1], edges[1][0], edges[1][1], edges[2][0], edges[2][1]
    l1, l2, l3 = pow(x2 - x1, 2) + pow(y2 - y1, 2), pow(x3 - x1, 2) + pow(y3 - y1, 2), pow(x3 - x2, 2) + pow(y3 - y2, 2)
    lenList = sorted([l1, l2, l3])
    if lenList[0] + lenList[1] != lenList[2] or lenList[0] != lenList[1]:
        print(0)
        return
    cases = list(combinations([0, 1, 2], 2))
    nBoard = [[0 for j in range(12)] for i in range(12)] # draw lines in this board
    for case in cases:
        p1, p2 = edges[case[0]], edges[case[1]]
        y1, x1, y2, x2 = p1[0], p1[1], p2[0], p2[1]
        if x1 == x2: #vertical
            for y in range(y1, y2 + 1):
                nBoard[y][x1] = 1
                if board[y][x1] != '1': # empty place is existing
                    print(0)
                    return
        else:
            m = (y2 - y1) / (x2 - x1)
            if m == 0 or m == 1 or m == -1:
                m = int(m)
                d = 0
            else:
                print(0)
                return
    for p in range(edges):
        print('%s %s' %(p[0], p[1]))


if __name__ == "__main__":
    main()
