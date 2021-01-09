import sys


def main():
    global N, nList, ans
    N = int(input())
    tList = list(map(int, sys.stdin.readline().split()))
    nList = []
    for i in range(N):
        nList.append([tList[i], i])
    nList.sort()
    ans = [0] * N
    ans[nList[0][1]] = 0
    bNum = nList[0][0]
    cnt = 1
    for i in range(1, N):
        cNum = nList[i][0] # 현재 값
        aIdx = nList[i][1] # ans에 집어넣을 idx
        if bNum == cNum:
            ans[aIdx] = cnt - 1
        else:# 값에 변화가 있음
            ans[aIdx] = cnt
            cnt += 1
            bNum = nList[i][0] #현재 값을 before number로 저장
    for i in range(N):
        print(ans[i], end=' ')


if __name__ == '__main__':
    main()
