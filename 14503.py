import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    rY, rX = r, c
    room = []
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline().split())))
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    chkDy = [0, -1, 0, 1]
    chkDx = [-1, 0, 1, 0]
    rCnt = 0 # 회전횟수
    cnt = 0
    while 1:
        if room[rY][rX] == 0:  # 청소안한 곳이면 청소
            room[rY][rX] = 8
            cnt += 1
        cY, cX = rY + chkDy[d], rX + chkDx[d]  # 왼쪽 칸 위치
        d -= 1  # 회전
        if d < 0:
            d = 3
        rCnt += 1
        if room[cY][cX] == 0:
            rY, rX = rY + dy[d], rX + dx[d]
            rCnt = 0
            continue
        else:  # 왼쪽 방향에 청소할 공간 없음
            if rCnt == 4: # 4방향 전부 다 청소공간 없음
                bd = (d + 2) % 4  # 뒤를 바라보게 함
                ny, nx = rY + dy[bd], rX + dx[bd]
                if room[ny][nx] != 1:
                    rY, rX = ny, nx
                    rCnt = 0
                    continue
                else:
                    print(cnt)
                    break
    return 0


if __name__ == "__main__":
    main()
