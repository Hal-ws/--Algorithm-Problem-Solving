import sys


def main():
    global ans, tracks
    N, M = map(int, sys.stdin.readline().split())
    ans = 0
    tracks = list(map(int, sys.stdin.readline().split()))
    right = sum(tracks)
    left = max(tracks)
    while left <= right:
        mid = (left + right) // 2
        tmp = chkposs(mid)
        if tmp[0] == M:
            if ans == 0:
                ans = tmp[1]
            else:
                if tmp[1] < ans:
                    ans = tmp[1]
            right -= 1
        if tmp[0] > M: # 사이즈를 늘려야됨
            left = mid + 1
        if tmp[0] < M: # 사이즈를 줄여야됨
            if ans == 0:
                ans = tmp[1]
            else:
                if tmp[1] < ans:
                    ans = tmp[1]
            right = mid - 1
    print(ans)


def chkposs(maxLen):
    global ans, tracks
    blueray = 0 # 현재 블루레이 안에 녹음된 길이
    cnt = 0 # 블루레이 숫자
    maxSize = 0
    for l in tracks:
        if blueray + l <= maxLen:
            if cnt == 0:
                cnt = 1
            blueray += l
        else:
            cnt += 1
            blueray = l
        if maxSize < blueray:
            maxSize = blueray
    return [cnt, maxSize] # 블루레이의 수, 개당 크기


if __name__ == '__main__':
    main()
