import sys
from collections import deque


def main():
    F, S, G, U, D = map(int, sys.stdin.readline().split())
    chk = [0] * (F + 1)
    q = deque()
    q.append([0, S])
    chk[S] = 1
    flag = 0
    while len(q) > 0:
        curP = q[0][1] # 현재위치
        curC = q[0][0] #현재까지 버튼 누른 횟수
        nU, nD = curP + U, curP - D
        if nU <= F and chk[nU] == 0:
            q.append([curC + 1, nU])
            chk[nU] = 1
        if nD > 0 and chk[nD] == 0:
            q.append([curC + 1, nD])
            chk[nD] = 1
        if curP == G:
            print(curC)
            flag = 1
            break
        q.popleft()
    if flag == 0:
        print("use the stairs")


if __name__ == '__main__':
    main()
