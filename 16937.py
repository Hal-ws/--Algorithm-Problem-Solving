import sys
from itertools import combinations


def main():
    global H, W, ans
    H, W = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    stickers = []
    for i in range(N):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    ans = 0
    idxList = [j for j in range(N)]
    cases = list(combinations(idxList, 2))
    for case in cases:
        s1, s2 = stickers[case[0]], stickers[case[1]]
        getans(s1[0], s1[1], s2[0], s2[1])
        getans(s1[0], s1[1], s2[1], s2[0])
        getans(s1[1], s1[0], s2[0], s2[1])
        getans(s1[1], s1[0], s2[1], s2[0])
    print(ans)


def getans(r1, c1, r2, c2): # s1, s2 크기정보
    global H, W, ans
    if H < r1 or H < r2: # 둘중 하나라도 세로 높이가 board 를 벗어날 때
        return 0
    if W < c1 or W < c2:
        return 0
    points = [[0, c1], [r1, 0], [r1, c1]]
    for p in points:
        y, x = p[0], p[1]
        if r2 <= H - y and c2 <= W - x:
            if ans <= r1 * c1 + r2 * c2:
                ans = r1 * c1 + r2 * c2
            return 0
    return 0


if __name__ == '__main__':
    main()
