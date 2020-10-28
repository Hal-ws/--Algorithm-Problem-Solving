from collections import deque


def main():
    S = int(input())
    q = deque()
    q.append([1, 0, 0]) ## 이모티콘 개수, 클립보드 저장, 시간
    visitChk = [0] * (2 * S + 1)
    visitChk[1] = 1
    while 1:
        if q[0][0] > 2:
            if visitChk[q[0][0] - 1] == 0:
                visitChk[q[0][0] - 1] = 1
                q.append([q[0][0] - 1, q[0][1], q[0][2] + 1])
                if q[0][0] - 1 == S:
                    ans = q[0][2] + 1
                    break
        if q[0][1] + q[0][0] <= 2 * S:
            if visitChk[q[0][1] + q[0][0]] == 0:
                visitChk[q[0][0] + q[0][1]] = 1
                q.append([q[0][0] + q[0][1], q[0][1], q[0][2] + 1])
                if q[0][0] + q[0][1] == S:
                    ans = q[0][2] + 1
                    break
        if q[0][0] * 2 <= 2 * S:
            if visitChk[q[0][0] * 2] == 0:
                visitChk[q[0][0] * 2] = 1
                q.append([q[0][0] * 2, q[0][0], q[0][2] + 2])
                if q[0][0] * 2 == S:
                    ans = q[0][2] + 2
                    break
        del q[0]
    print(ans)


if __name__ == "__main__":
    main()
