def main():
    global N, buildings
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for sIdx in range(N):
        tmp = watchleft(sIdx) + watchright(sIdx)
        if ans < tmp:
            ans = tmp
    print(ans)


def watchleft(sIdx):
    global buildings
    cnt = 0
    for i in range(sIdx):
        dy = buildings[sIdx] - buildings[i]
        dx = sIdx - i
        flag = 1
        for j in range(i + 1, sIdx): # 사이에 있는 빌딩중 시야를 가리는게 있는지 확인
            h = buildings[j]
            if dy * (j - i) + dx * buildings[i] <= h * dx:
                flag = 0
                break
        if flag:
            cnt += 1
    return cnt


def watchright(sIdx):
    global N, buildings
    cnt = 0
    for i in range(sIdx + 1, N):
        dy = buildings[i] - buildings[sIdx]
        dx = i - sIdx
        flag = 1
        for j in range(sIdx + 1, i):
            h = buildings[j]
            if dy * (j - i) + dx * buildings[i] <= h * dx:
                flag = 0
                break
        if flag:
            cnt += 1
    return cnt


if __name__ == '__main__':
    main()
