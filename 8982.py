import sys


def main():
    N = int(sys.stdin.readline())
    pool = [0] * 40001
    points = []
    for i in range(N):
        x, d = map(int, sys.stdin.readline().split())
        points.append([x, d])
        if i >= 2:
            if points[i - 1][1] == points[i][1]:
                for j in range(points[i - 1][0], points[i][0]):
                    pool[j] = points[i - 1][1]
        if i == N - 1:
            lastX = x
    pool = pool[:lastX]
    l = len(pool)
    drained = [0] * l # 빠져나간 물의 높이
    holes = []
    M = int(sys.stdin.readline())
    for i in range(M):
        holes.append(list(map(int, sys.stdin.readline().split())))
    for h in holes:
        x1, x2, depth1, depth2 = h[0], h[2], h[1], h[3]
        for j in range(x1, x2):
            if drained[j] < depth1: #depth만큼 빼줌
                drained[j] += (depth1 - drained[j])
        for j in range(x1 - 1, -1, -1): #왼쪽으로 이동
            if depth1 <= pool[j]: #같거나 더 깊은곳으로 갈때
                if drained[j] <= depth1: # 빠져나갈 물이 남아있을때
                    drained[j] += (depth1 - drained[j])
            else:# 더 얕은 곳으로 갈때
                depth1 = pool[j] # 빠져나갈 수 있는 깊이 수정
                if drained[j] <= depth1:
                    drained[j] += (depth1 - drained[j])
        for j in range(x2, l): # 오른쪽으로 이동
            if depth2 <= pool[j]: # 같거나 더 깊은곳으로 갈때
                if drained[j] <= depth2:
                    drained[j] += (depth2 - drained[j])
            else: #얕은곳으로 갈때
                depth2 = pool[j]
                if drained[j] <= depth2:
                    drained[j] += (depth2 - drained[j])
    ans = 0
    for i in range(l):
        ans += (pool[i] - drained[i])
    print(ans)


if __name__ == '__main__':
    main()
