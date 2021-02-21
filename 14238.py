def main():
    global ansl
    a = input()
    ansl = len(a)
    ans = -1
    cCnt = [0, 0, 0] # a, b, c 기록
    for c in a:
        cCnt[ord(c) - 65] += 1
    for i in range(3):
        if cCnt[i] > 0:
            tmp = getans(i, [cCnt[0], cCnt[1], cCnt[2]])
            if tmp != -1:
                ans = tmp
                break
    print(ans)

def getans(sIdx, cntList):
    global ansl
    word = chr(sIdx + 65)
    cntList[sIdx] -= 1
    dis = [51, 51, 51] # A로부터 거리, B로부터 거리, C로부터 거리
    dis[sIdx] = 0 # 붙어있음
    while 1:
        if len(word) == ansl:
            return word
        left = ansl - len(word) - 1 # 지금 시행에서 붙이고 남은 길이
        maxB = left // 2 #B를 붙일 수 있는 최대 갯수
        maxC = left // 3 #C를 붙일 수 있는 최대 갯수
        if left % 2 != 0:
            maxB += 1
        if left % 3 != 0:
            maxC += 1
        # C붙임
        if cntList[2] > 0 and cntList[1] <= maxB and dis[2] >= 2:
            word += 'C'
            cntList[2] -= 1
            dis[0], dis[1], dis[2] = dis[0] + 1, dis[1] + 1, 0
            continue
        if cntList[1] > 0 and cntList[2] <= maxC and dis[1] >= 1:
            word += 'B'
            cntList[1] -= 1
            dis[0], dis[1], dis[2] = dis[0] + 1, 0, dis[2] + 1
            continue
        if cntList[0] > 0:
            word += 'A'
            cntList[0] -= 1
            dis[0], dis[1], dis[2] = 0, dis[1] + 1, dis[2] + 1
            continue
        break
    return -1


if __name__ == '__main__':
    main()
