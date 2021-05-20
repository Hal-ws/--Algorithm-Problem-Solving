import sys


def main():
    M, N = map(int, sys.stdin.readline().split())
    if M == N:
        sCnt = M // 2
        if M % 2 == 0:
            sCnt = M // 2  # 그리는 사각형의 갯수
            print(sCnt * 4 - 1)
            print('%s %s' %(sCnt + 2, sCnt + 1))
        else:
            print(sCnt * 4)
            print('%s %s' %(sCnt + 2, sCnt + 2))
    else:
        sCnt = min(M, N) // 2
        if M > N: # 세로가 더 긴경우
            if N % 2 == 1: # 내려가는걸로 끝
                print(sCnt * 4 + 1)
                print('%s %s' %(M - sCnt, sCnt + 1))
            else: # 올라오는걸로 끝
                print(sCnt * 4 - 1)
                print('%s %s' %(sCnt + 1, sCnt))
        else: # 가로가 더 긴경우
            if M % 2 == 1: # 오른쪽 이동으로 끝
                print(sCnt * 4)
                print('%s %s' %(sCnt + 1, N - sCnt))
            else: # 왼쪽 이동으로 끝
                print(sCnt * 4 - 2)
                print('%s %s' %(sCnt + 1, sCnt))


if __name__ == '__main__':
    main()
