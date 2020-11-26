import sys
from collections import deque


def main():
    R, C, T = map(int, sys.stdin.readline().split())
    room = []
    for i in range(R):
        room.append(list(map(int, sys.stdin.readline().split()))) ##이상 x
    for i in range(R):
        if room[i][0] == -1:
            acPos = i
            break
    for i in range(T):
        disperse(room, R, C)
        circulation(room, R, C, acPos)
    ans = 0
    for i in range(R):
        ans += sum(room[i])
    print(ans + 2)


def disperse(room, R, C):
    variance = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] >= 5:
                if i > 0 and room[i - 1][j] != -1:
                    variance[i - 1][j] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
                if i < R - 1 and room[i + 1][j] != -1:
                    variance[i + 1][j] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
                if j > 0 and room[i][j - 1] != -1:
                    variance[i][j - 1] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
                if j < C - 1 and room[i][j + 1] != -1:
                    variance[i][j + 1] += room[i][j] // 5
                    variance[i][j] -= (room[i][j] // 5)
    for i in range(R):
        for j in range(C):
            room[i][j] += variance[i][j]
3

def circulation(room, R, C, acPos):
    # 시계방향(에어컨 아래쪽)
    lUy, lUx = acPos + 1, 0
    rDy, rDx = R - 1, C - 1
    q = deque()
    for i in range(1, rDx + 1):
        q.append(room[lUy][i])
    for i in range(lUy + 1, rDy + 1):
        q.append(room[i][rDx])
    for i in range(rDx - 1, -1, -1):
        q.append(room[rDy][i])
    for i in range(rDy - 1, lUy, -1):
        q.append(room[i][lUx])
    q.appendleft(0)  # 깨끗한 공기가 들어감
    q.pop() #청정기로 들어감
    for i in range(1, rDx + 1):
        room[lUy][i] = q.popleft()
    for i in range(lUy + 1, rDy + 1):
        room[i][rDx] = q.popleft()
    for i in range(rDx - 1, -1, -1):
        room[rDy][i] = q.popleft()
    for i in range(rDy - 1, lUy, -1):
        room[i][lUx] = q.popleft()
    #시계방향, 에어컨 위쪽
    lUy, lUx = 0, 0
    rDy, rDx = acPos, C - 1
    q = deque()
    for i in range(1, rDx + 1):
        q.append(room[rDy][i])
    for i in range(rDy - 1, -1, -1):
        q.append(room[i][rDx])
    for i in range(rDx - 1, -1, -1):
        q.append(room[lUy][i])
    for i in range(1, rDy):
        q.append(room[i][lUx])
    q.appendleft(0)
    q.pop()
    for i in range(1, rDx + 1):
        room[rDy][i] = q.popleft()
    for i in range(rDy - 1, -1, -1):
        room[i][rDx] = q.popleft()
    for i in range(rDx - 1, -1, -1):
        room[lUy][i] = q.popleft()
    for i in range(1, rDy):
        room[i][lUx] = q.popleft()


if __name__ == "__main__":
    main()
