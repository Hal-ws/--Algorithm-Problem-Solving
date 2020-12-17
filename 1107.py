import sys


def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    if M > 0:
        broken = list(map(int, sys.stdin.readline().split()))
    button = [1] * 10
    for i in range(M):
        button[broken[i]] = 0
    ans1 = abs(N - 100)
    ans2= 500000
    minDis = 1000000
    for i in range(1000001):
        tmp = getnear(i, button)
        if tmp != None:
            dis = + abs(N - i)
            tmp = tmp + dis
            if tmp <= ans2:
                ans2 = tmp
            if dis <= minDis: #거리가 멀어지면 제일 가까운 값이 아니기 때문에 break 해준다
                minDis = dis 
            else:
                break
    print(min(ans1, ans2))


def getnear(N, button):
    flag = 1
    cnt = 0
    if N == 0:
        if button[0]:
            return 1
        return 500000
    while N > 0:
        tmp = N % 10
        if button[tmp] == 0: # 버튼 고장남
            flag = 0
            break
        cnt += 1 #해당 위치의 숫자를 버튼으로 누를수 있음
        N = N // 10
    if flag:
        return cnt
    else:
        return None


if __name__ == '__main__':
    main()
