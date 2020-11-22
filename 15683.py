import sys
from itertools import product

def main():
    N, M = map(int, sys.stdin.readline().split())
    room = []
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline().split())))
    cameras = []
    for i in range(N):
        for j in range(M):
            if room[i][j] != 0 and room[i][j] != 6 and room[i][j] != 5:
                cameras.append([room[i][j], i, j]) # 카메라종류, i, j 표시
            if room[i][j] == 5: # 방향전환 할필요없이 바로 감시
                watch5(room, i, j, N, M)
    cameras.sort()
    direction = list(product([0, 1, 2, 3], repeat=len(cameras)))
    ld = len(direction)
    minVal = 64
    for i in range(ld):
        temp = case(room, cameras, i, direction[i], N, M) ## 각 방향대로 카메라 값 설정
        if temp <= minVal:
            minVal = temp
    print(cameras)


def case(room, camera, idx, direction, N, M):
    for i in range(direction):
        if camera[idx][0] == 1:
            watch1(room, direction[i], [camera[idx][1], camera[idx][2]], N, M)
        if camera[idx][0] == 2:
            








def watch1()


def watch5(room, posy, posx, N, M):
    for i in range(posy - 1, -1, -1):
        if room[i][posx] == 6:
            break
        room[i][posx] = '#'
    for i in range(posy + 1, N):
        if room[i][posx] == 6:
            break
        room[i][posx] = '#'
    for i in range(posx - 1, -1, -1):
        if room[posy][i] == 6:
            break
        room[posy][i] = '#'
    for i in range(posx + 1, M):
        if room[posy][i] == 6:
            break
        room[posy][i] = '#'





if __name__ == "__main__":
    main()
