import sys


def main():
    N, T = map(int, sys.stdin.readline().split())
    cityInfo = [[] for i in range(N + 1)]
    disMatrix = [[0 for j in range(N + 1)] for i in range(N + 1)]
    nearSpecialCity = [0 for i in range(N + 1)]
    for i in range(1, N + 1):
        cityInfo[i] = list(map(int, sys.stdin.readline().split()))
    for i in range(1, N + 1):
        nearDis = 2001
        for j in range(1, N + 1):
            if cityInfo[j][0]:
                tDis = abs(cityInfo[i][1] - cityInfo[j][1]) + abs(cityInfo[i][2] - cityInfo[j][2])
                if tDis < nearDis:
                    nearDis = tDis
                    nearSpecialCity[i] = j # i city와 가장 가까운 special city는 j (자기자신이 될수도 있음)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                chk1, chk2 = cityInfo[i][0], cityInfo[j][0]
                if chk1 == chk2 == 1:
                    dis = getDis(cityInfo, i, j, T)
                else:
                    dis = normalCity(cityInfo, i, j, T, nearSpecialCity)
                disMatrix[i][j] = dis
                disMatrix[j][i] = dis
    M = int(sys.stdin.readline())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        print(disMatrix[a][b])


def getDis(cityInfo, a, b, T):
    x1, y1, x2, y2 = cityInfo[a][1], cityInfo[a][2], cityInfo[b][1], cityInfo[b][2]
    if cityInfo[a][0] == cityInfo[b][0] == 1:
        return min(abs(x2 - x1) + abs(y2 - y1), T)
    else:
        return abs(x2 - x1) + abs(y2 - y1)


def normalCity(cityInfo, a, b, T, nearSpecialCity):
    dis1 = getDis(cityInfo, a, b, T) # 다이렉트로 감
    dis2 = 2001 # teleport city를 통해서 감
    if nearSpecialCity[a] != 0: # special city가 존재할 경우
        p1, p2 = nearSpecialCity[a], nearSpecialCity[b] #
        tmpDis = getDis(cityInfo, a, p1, T)
        tmpDis += getDis(cityInfo, p1, p2, T)
        tmpDis += getDis(cityInfo, p2, b, T)
        dis2 = min(dis2, tmpDis)
    return min(dis1, dis2)


if __name__ == '__main__':
    main()
