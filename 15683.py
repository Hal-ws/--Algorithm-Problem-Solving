import sys
from itertools import product


def main():
    N, M = map(int, sys.stdin.readline().split())
    room = []
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline().split())))
    cameras14 = [] #1~4번 카메라까지만 저장
    camera5 = []
    hole = 0 #감시 못하는 공간의 크기
    for i in range(N):
        for j in range(M):
            if 1 <= room[i][j] <5:
                cameras14.append([room[i][j], i, j])
            if room[i][j] == 5:
                camera5.append([i, j])
            if room[i][j] == 0: #관찰가능한 공간 찾음
                hole += 1
    l14 = len(cameras14) #1~4번 카메라의 개수
    case = list(product([0, 1, 2, 3], repeat = l14)) #1,2,3,4 카메라들의 방향(0,1,2,3) 경우의 수 저장
    for i in range(len(camera5)): # 카메라5는 방향 없으므로 미리 검사한다
        hole -= watching5(camera5[i][0], camera5[i][1], room, N, M)
    lc = len(case)
    maxCnt = 0#감시 가능한 구역의 최대 수
    for i in range(lc):
        chk = [[0 for j in range(M)] for k in range(N)] #이미 감시한 지역인지 확인
        tmpCnt = 0
        for j in range(l14): #i번 케이스의 j번 카메라에 대해서 수행
            camera = cameras14[j]
            if camera[0] == 1:
                tmpCnt += watching1(camera[1], camera[2], room, case[i][j],chk, N, M)
            if camera[0] == 2:
                tmpCnt += watching2(camera[1], camera[2], room, case[i][j], chk, N, M)
            if camera[0] == 3:
                tmpCnt += watching3(camera[1], camera[2], room, case[i][j], chk, N, M)
            if camera[0] == 4:
                tmpCnt += watching4(camera[1], camera[2], room, case[i][j], chk, N, M)
        if tmpCnt >= maxCnt:
            maxCnt = tmpCnt
    print(hole - maxCnt)


# 5번 카메라로 감시
def watching5(y, x, room, N, M):
    i = 1
    cnt = 0
    while 1:
        if y + i == N:
            break
        if room[y + i][x] == 6:
            break
        if room[y + i][x] == 0:
            room[y + i][x] = "#"
            cnt += 1 #감시가능영역 늘림
        i += 1
    i = 1
    while 1:
        if y - i == -1:
            break
        if room[y - i][x] == 6:
            break
        if room[y - i][x] == 0:
            room[y - i][x] = "#"
            cnt += 1
        i += 1
    j = 1
    while 1:
        if x + j == M:
            break
        if room[y][x + j] == 6:
            break
        if room[y][x + j] == 0:
            room[y][x + j] = "#"
            cnt += 1
        j += 1
    j = 1
    while 1:
        if x - j == -1:
            break
        if room[y][x - j] == 6:
            break
        if room[y][x - j] == 0:
            room[y][x - j] = "#"
            cnt += 1
        j += 1
    return cnt


def watching1(y, x, room, d, chk, N, M):
    cnt = 0
    if d == 0:
        cnt = rightchk(y, x, room, chk, N, M)
    if d == 1:
        cnt = downchk(y, x, room, chk, N, M)
    if d == 2:
        cnt = leftchk(y, x, room, chk, N, M)
    if d == 3:
        cnt = upchk(y, x, room, chk, N, M)
    return cnt # 카메라로 감시 가능한 수


def watching2(y, x, room, d, chk, N, M):
    cnt = 0
    if d == 0 or d == 2:
        cnt += rightchk(y, x, room, chk, N, M)
        cnt += leftchk(y, x, room, chk, N, M)
    if d == 1 or d == 3:
        cnt += downchk(y, x, room, chk, N, M)
        cnt += upchk(y, x, room, chk, N, M)
    return cnt


def watching3(y, x, room, d, chk, N, M):
    cnt = 0
    if d == 0:
        cnt += upchk(y, x, room, chk, N, M)
        cnt += rightchk(y, x, room, chk, N, M)
    if d == 1:
        cnt += rightchk(y, x, room, chk, N, M)
        cnt += downchk(y, x, room, chk, N, M)
    if d == 2:
        cnt += downchk(y, x, room, chk, N, M)
        cnt += leftchk(y, x, room, chk, N, M)
    if d == 3:
        cnt += leftchk(y, x, room, chk, N, M)
        cnt += upchk(y, x, room, chk, N, M)
    return cnt


def watching4(y, x, room, d, chk, N, M):
    cnt = 0
    if d == 0:
        cnt += leftchk(y, x, room, chk, N, M)
        cnt += upchk(y, x, room, chk, N, M)
        cnt += rightchk(y, x, room, chk, N, M)
    if d == 1:
        cnt += upchk(y, x, room, chk, N, M)
        cnt += rightchk(y, x, room, chk, N, M)
        cnt += downchk(y, x, room, chk, N, M)
    if d == 2:
        cnt += rightchk(y, x, room, chk, N, M)
        cnt += downchk(y, x, room, chk, N, M)
        cnt += leftchk(y, x, room, chk, N, M)
    if d == 3:
        cnt += downchk(y, x, room, chk, N, M)
        cnt += leftchk(y, x, room, chk, N, M)
        cnt += upchk(y, x, room, chk, N, M)
    return cnt


def upchk(y, x, room, chk, N, M):
    cnt = 0
    i = 1
    while 1:
        if y - i == -1:
            break
        if room[y - i][x] == 6:
            break
        if room[y - i][x] == 0 and chk[y - i][x] == 0:
            chk[y - i][x] = 1
            cnt += 1
        i += 1
    return cnt


def rightchk(y, x, room, chk, N, M):
    cnt = 0
    j = 1
    while 1:
        if x + j == M:
            break
        if room[y][x + j] == 6:
            break
        if room[y][x + j] == 0 and chk[y][x + j] == 0:
            chk[y][x + j] = 1
            cnt += 1
        j += 1
    return cnt


def downchk(y, x, room, chk, N, M):
    cnt = 0
    i = 1
    while 1:
        if y + i == N:
            break
        if room[y + i][x] == 6:
            break
        if room[y + i][x] == 0 and chk[y + i][x] == 0:
            chk[y + i][x] = 1
            cnt += 1
        i += 1
    return cnt


def leftchk(y, x, room, chk, N, M):
    cnt = 0
    j = 1
    while 1:
        if x - j == -1:
            break
        if room[y][x - j] == 6:
            break
        if room[y][x - j] == 0 and chk[y][x - j] == 0:
            chk[y][x - j] = 1
            cnt += 1
        j += 1
    return cnt


if __name__ == "__main__":
    main()
