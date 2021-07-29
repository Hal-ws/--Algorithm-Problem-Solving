import sys


def main():
    N, L = map(int, sys.stdin.readline().split())
    floors = []
    for i in range(N):
        l, d = map(int, sys.stdin.readline().split())
        if d: # 오른쪽에서 왼쪽으로 이동
            floors.append([L - l, L, d]) # 왼쪽, 오른쪽 끝, 방향
        else:
            floors.append([0, l, d])
    t = 0
    pos = 0 # 0층에 있음
    while 1:
        pos = up(pos, floors, N) # 올라갈수 있는지 확인후 움직임
        moving(floors, N, L) # 사다리들을 움직임
        if pos == N - 1:
            break
        t += 1
    print(t)


def moving(floors, N, L): # floors에 있는 것들을 움직임
    for i in range(N):
        left, right, d = floors[i][0], floors[i][1], floors[i][2]
        if floors[i][2]: # 왼쪽으로 이동
            if left == 0:  # 사다리를 오른쪽으로 이동후 방향도 변경
                if floors[i][1] < L: # 오른쪽으로 이동가능할때
                    floors[i][0] += 1
                    floors[i][1] += 1
                    floors[i][2] = 0
            else: # 사다리를 계속 왼쪽으로 이동
                floors[i][0] -= 1
                floors[i][1] -= 1
        else: # 오른쪽으로 이동
            if right == L: # 사다리를 왼쪽으로 이동후 방향도 변경
                if floors[i][0] > 0:
                    floors[i][0] -= 1
                    floors[i][1] -= 1
                    floors[i][2] = 1
            else: # 사다리를 계속 오른쪽으로 이동
                floors[i][0] += 1
                floors[i][1] += 1


def up(pos, floors, N):
    arrive = pos
    for curP in range(pos, N - 1): # curP층에서 curP + 1층을 올라갈수 있는지 확인함
        l1, r1 = floors[curP][0], floors[curP][1]
        l2, r2 = floors[curP + 1][0], floors[curP + 1][1]
        if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
            arrive = curP + 1 # 위층으로 도달가능
        else:
            break
    return arrive


if __name__ == "__main__":
    main()
