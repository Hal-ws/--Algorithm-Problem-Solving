import sys
from collections import deque
def main():
    n, m = map(int, sys.stdin.readline().split())
    sumofcheese, plate = 0, []
    for i in range(n):
        plate.append(list(map(int, sys.stdin.readline().split())))
        sumofcheese += sum(plate[i])
    leftcheese = [sumofcheese]
    i = 1
    while True:
        leftcheese.append(melting(n, m, plate, leftcheese[i - 1]))
        if leftcheese[i] == 0:
            break
        i += 1
    print(i)
    print(leftcheese[i - 1])


def melting(n, m, plate, leftcheese):
    q = deque()
    q.append([0, 0])
    meltingChk = [[0 for i in range(m)] for j in range(n)]
    visitChk = [[0 for i in range(m)] for j in range(n)]
    visitChk[0][0] = 1
    while len(q) > 0:
        if q[0][0] < n - 1:
            if plate[q[0][0] + 1][q[0][1]] == 1 and meltingChk[q[0][0] + 1][q[0][1]] == 0:
                meltingChk[q[0][0] + 1][q[0][1]] = 1
                leftcheese -= 1
            if plate[q[0][0] + 1][q[0][1]] == 0 and visitChk[q[0][0] + 1][q[0][1]] == 0:
                q.append([q[0][0] + 1, q[0][1]])
                visitChk[q[0][0] + 1][q[0][1]] = 1
        if q[0][0] > 0:
            if plate[q[0][0] - 1][q[0][1]] == 1 and meltingChk[q[0][0] - 1][q[0][1]] == 0:
                meltingChk[q[0][0] - 1][q[0][1]] = 1
                leftcheese -= 1
            if plate[q[0][0] - 1][q[0][1]] == 0 and visitChk[q[0][0] - 1][q[0][1]] == 0:
                q.append([q[0][0] - 1, q[0][1]])
                visitChk[q[0][0] - 1][q[0][1]] = 1
        if q[0][1] < m - 1:
            if plate[q[0][0]][q[0][1] + 1] == 1 and meltingChk[q[0][0]][q[0][1] + 1] == 0:
                meltingChk[q[0][0]][q[0][1] + 1] = 1
                leftcheese -= 1
            if plate[q[0][0]][q[0][1] + 1] == 0 and visitChk[q[0][0]][q[0][1] + 1] == 0:
                q.append([q[0][0], q[0][1] + 1])
                visitChk[q[0][0]][q[0][1] + 1] = 1
        if q[0][1] > 0:
            if plate[q[0][0]][q[0][1] - 1] == 1 and meltingChk[q[0][0]][q[0][1] - 1] == 0:
                meltingChk[q[0][0]][q[0][1] - 1] = 1
                leftcheese -= 1
            if plate[q[0][0]][q[0][1] - 1] == 0 and visitChk[q[0][0]][q[0][1] - 1] == 0:
                q.append([q[0][0], q[0][1] - 1])
                visitChk[q[0][0]][q[0][1] - 1] = 1
        q.popleft()
    for i in range(n):
        for j in range(m):
            if meltingChk[i][j]:
                plate[i][j] = 0
    return leftcheese
if __name__ == "__main__":
    main()
