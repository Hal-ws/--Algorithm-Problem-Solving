import sys


def main():
    fishes = []
    directions = []
    for i in range(4):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmpfish = [tmp[0], tmp[2], tmp[4], tmp[6]]
        tmpdir = [tmp[1], tmp[3], tmp[5], tmp[7]]
        fishes.append(tmpfish)
        directions.append(tmpdir)
    fishespos = [0] * 17 #1번 물고기부터 16번 물고기까지 위치 기록
    for i in range(4):
        for j in range(4):
            fishespos[fishes[i][j]] = [i, j]
    fishespos[fishes[0][0]] = 0 #상어한테 잡아먹혀서 [0, 0]에 있던 물고기는 지워짐
    sumEat = fishes[0][0] # 잡아먹은것 기록
    fishes[0][0] = '*' #fishes에서 상어는 *로 표시
    maxVal = [0]
    print('1')
    sharksmove(fishes, directions, fishespos, [0, 0], sumEat, maxVal)
    print(maxVal[0])


def sharksmove(fishes, directions, fishespos, pos, sumEat, maxVal): # cnt: 지금까지 잡아먹은 물고기 번호의 합
    fishesmove(fishes, directions, fishespos)
    y, x = pos[0], pos[1]
    flag = 0 # 먹이를 찾았는지 확인
    sDir = directions[y][x] # 잡아먹은 물고기 방향 받음\
    for i in range(4):
        print(fishes[i])
    print('********************')
    print('direction')
    for i in range(4):
        print(directions[i])

    print('------------------------------')
    if sDir == 1:
        for i in range(1, 5):
            ny, nx = y - i, x
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][x] != 0: #밖으로 나가지 않고 빈칸이 아닐때(물고기 잡아먹을수 있을때)
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 2:
        for i in range(1, 5):
            ny, nx = y - i, x - i
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 3:
        for i in range(1, 5):
            ny, nx = y, x - i
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 4:
        for i in range(1, 5):
            ny, nx = y + i, x - i
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 5:
        for i in range(1, 5):
            ny, nx = y + i, x
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 6:
        for i in range(1, 5):
            ny, nx = y + i, x + i
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 7:
        for i in range(1, 5):
            ny, nx = y, x + i
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if sDir == 8:
        for i in range(1, 5):
            ny, nx = y - i, x + i
            if 0 <= ny < 4 and 0 <= nx < 4and fishes[ny][nx] != 0:
                flag = 1
                prey = fishes[ny][nx]
                fishes[ny][nx] = '*'
                fishes[y][x] = 0 # 상어가 자리옮겨서 비워짐
                fishespos[prey] = 0 #잡아먹혔으니 fishespos에서 없어짐
                sumEat += prey
                sharksmove(fishes, directions, fishespos, [ny, nx], sumEat, maxVal)
                #백트래킹. 다시 돌아옴
                fishes[ny][nx] = prey
                fishes[y][x] = '*'
                fishespos[prey] = [ny, nx]
                sumEat -= prey
    if flag == 0: #더이상 먹이를 못찾으면 최대값과 비교한다
        if maxVal[0] <= sumEat:
            maxVal[0] = sumEat
        return 0


def fishesmove(fishes, directions, fishespos):
    for i in range(1, 17):
        if fishespos[i] != 0: #i번 fish가 아직 안잡아먹혔을때
            findtarget(fishes, directions, fishespos, i) #각 물고기들이 빙글빙글 돌면서 교체 가능한 지역을 찾는다


def findtarget(fishes, directions, fishespos, movingfish):
    cnt = 0
    y, x = fishespos[movingfish][0], fishespos[movingfish][1]
    dir = directions[y][x]
    flag = 0 #타겟을 찾음
    while cnt < 8: # 방향을 7번까지만 바꾼다
        if dir == 1:
            if 0 <= y - 1 and fishes[y - 1][x] != "*": # 이동할 수 있는 지점 확인
                target = [y - 1, x]
                flag = 1
                break #
            cnt, dir = cnt + 1, dir + 1
        if dir == 2:
            if 0 <= y - 1 and 0 <= x - 1 and fishes[y - 1][x - 1] != "*":
                target = [y - 1, x - 1]
                flag = 1
                break
            cnt, dir = cnt + 1, dir + 1
        if dir == 3:
            if 0 <= x - 1 and fishes[y][x - 1] != "*":
                target = [y, x - 1]
                flag = 1
                break
            cnt, dir = cnt + 1, dir + 1
        if dir == 4:
            if y + 1 < 4 and 0 <= x - 1 and fishes[y + 1][x - 1] != '*':
                target = [y + 1, x - 1]
                flag = 1
                break
            cnt, dir = cnt + 1, dir + 1
        if dir == 5:
            if y + 1 < 4 and fishes[y + 1][x] != '*':
                target = [y + 1, x]
                flag = 1
                break
            cnt, dir = cnt + 1, dir + 1
        if dir == 6:
            if y + 1 < 4 and x + 1 < 4 and fishes[y + 1][x + 1] != '*':
                target = [y + 1, x + 1]
                flag = 1
                break
            cnt, dir = cnt + 1, dir + 1
        if dir == 7:
            if x + 1 < 4 and fishes[y][x + 1] != '*':
                target = [y, x + 1]
                flag = 1
                break
            cnt, dir = cnt + 1, dir + 1
        if dir == 8:
            if 0 <= y - 1 and x + 1 < 4 and fishes[y - 1][x + 1] != "*":
                target = [y - 1, x + 1]
                flag = 1
                break
            cnt, dir = cnt + 1, 1
    if flag:
        targetfish = fishes[target[0]][target[1]]
        fishes[y][x], fishes[target[0]][target[1]] = fishes[target[0]][target[1]], fishes[y][x] #fishes에서 위치 교체
        fishespos[movingfish], fishespos[targetfish] = fishespos[targetfish], fishespos[movingfish]
        directions[y][x] = directions[target[0]][target[1]]
        directions[target[0]][target[1]] = dir


if __name__ == "__main__":
    main()
