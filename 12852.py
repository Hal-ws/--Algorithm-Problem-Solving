import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    q = deque()
    visit = [0] * (N + 1)
    visit[N] = 1
    q.append([[N], 0])
    while len(q) > 0:
        nums = q[0][0]
        cnt = q[0][1]
        cur = nums[cnt]
        if cur == 1:
            ansCnt = q[0][1]
            ans = nums
            break
        if cur % 3 == 0 and visit[cur // 3] == 0:
            q.append([nums + [cur // 3], cnt + 1])
            visit[cur // 3] = 1
        if cur % 2 == 0 and visit[cur // 2] == 0:
            q.append([nums + [cur // 2], cnt + 1])
            visit[cur // 2] = 1
        if visit[cur - 1] == 0:
            q.append([nums + [cur - 1] , cnt + 1])
            visit[cur - 1] = 1
        q.popleft()
    print(ansCnt)
    for num in ans:
        print(num, end=' ')


if __name__ == '__main__':
    main()
