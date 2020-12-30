import sys


def main():
    N, S = map(int, sys.stdin.readline().split())
    series = list(map(int, sys.stdin.readline().split()))
    start, end = 0, 0
    tmp, ans = series[0], 1000001
    while 1:
        if tmp == S:
            if end - start + 1 <= ans:
                ans = end - start + 1
            if end == N - 1: #더 이상 답되는거 없다.
                break
            else:
                end += 1
                tmp += series[end]
        elif S < tmp: # first 를 한칸 옮겨도 되는지 확인
            if end - start + 1 <= ans:
                ans = end - start + 1
            if start == end:
                if end == N - 1:
                    break
                else:
                    end += 1
                    tmp += series[end]
            else:
                tmp -= series[start]
                start += 1
        else:
            if end == N - 1:
                break
            else:
                end += 1
                tmp += series[end]
    if ans == 1000001:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
