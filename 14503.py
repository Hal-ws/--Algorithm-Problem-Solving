import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    r, c, d= map(int, sys.stdin.readline().split())
    room = []
    robot = [r, c, d, 0, 1] # 위치(r, c) d(방향), 현 위치에서 청소 불가능한 인접 block 수, 청소한 블록수
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline().split())))
    room[r][c] = 9 # 시작지점 청소함(청소한 칸: 9)
    while 1:
        if acting(room, robot) == 0:
            break
    print(robot[4])


def acting(room, robot):
    robot[3] = 0
    for i in range(4):
        if robot[2] == 1:
            if room[robot[0] - 1][robot[1]] == 0:
                robot[2], robot[0], robot[4] = 0, robot[0] - 1, robot[4] + 1
                break
            else:
                robot[2], robot[3] = 0, robot[3] + 1
        elif robot[2] == 2:
            if room[robot[0]][robot[1] + 1] == 0:
                robot[2], robot[1], robot[4] = 1, robot[1] + 1, robot[4] + 1
                break
            else:
                robot[2], robot[3] = 1, robot[3] + 1
        elif robot[2] == 3:
            if room[robot[0] + 1][robot[1]] == 0:
                robot[2], robot[0], robot[4] = 2, robot[0] + 1, robot[4] + 1
                break
            else:
                robot[2], robot[3] = 2, robot[3] + 1
        elif robot[2] == 0:
            if room[robot[0]][robot[1] - 1] == 0:
                robot[2], robot[1], robot[4] = 3, robot[1] - 1, robot[4] + 1
                break
            else:
                robot[2], robot[3] = 3, robot[3] + 1
    room[robot[0]][robot[1]] = 9 # 움직인 부분 청소
    if robot[3] == 4: ## 지금 위치에서 더 이상 청소할 데 없음. 후진 프로세스
        if robot[2] == 1:
            if room[robot[0]][robot[1] - 1] != 1: # 뒤로갈 공간 있음
                robot[1] -= 1
            else: #없음
                return 0
        if robot[2] == 2:
            if room[robot[0] - 1][robot[1]] != 1:
                robot[0] -= 1
            else:
                return 0
        if robot[2] == 3:
            if room[robot[0]][robot[1] + 1] != 1:
                robot[1] += 1
            else:
                return 0
        if robot[2] == 0:
            if room[robot[0] + 1][robot[1]] != 1:
                robot[0] += 1
            else:
                return 0


if __name__ == "__main__":
    main()
