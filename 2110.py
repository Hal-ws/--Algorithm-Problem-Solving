import sys


def main():
    global N, C, house
    ans = 0
    N, C = map(int, sys.stdin.readline().split())
    house = [0] * N
    for i in range(N):
        house[i] = int(sys.stdin.readline())
    house = sorted(house)
    left, right = 1, (house[N - 1] - house[0]) // (C - 1) # 최소, 최대 간격
    while left <= right:
        mid = (left + right) // 2
        if setWIFI(mid): #배치 가능한경우. 더 넓게 배치해본다
            if ans < mid:
                ans = mid
            left = mid + 1
        else: # 배치 불가능. 더 좁게 배치해본다.
            right = mid - 1
    print(ans)


def setWIFI(dis):
    cnt = 1
    nearI = 0 # 가장 가까운 wifi의 idx
    for i in range(1, N):
        if dis <= house[i] - house[nearI]: # 배치 가능
            cnt += 1
            nearI = i
        if cnt == C: # C개 배치 성공
            return 1
    return 0 # 실패


if __name__ == "__main__":
    main()
