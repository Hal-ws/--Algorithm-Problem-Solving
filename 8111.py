import sys
from collections import deque


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        q = deque()
        ans = None
        for j in range(1, 10):
            if (N * j) % 10 == 1 or (N * j) % 10 == 0:
                q.append([str(j), 1, len(str(N))])
        while len(q) > 0:
            mVal, l, lenN = q[0][0], q[0][1], q[0][2] # 약수, 정해진 자릿수의 길이, 현재 값의 길이
            if lenN > 100:
                q.popleft()
                continue
            num = N * int(mVal)
            if l == lenN:
                ans = num
            sNum = str(num)
            ansFlag = 1
            for j in range(lenN - l - 1, -1, -1):
                if sNum[j] != '1' and sNum[j] != '0':
                    ansFlag = 0
            if ansFlag: #답이 될 때
                ans = sNum
                break
            for j in range(1, 10): #
                tmp = num + (N * j * pow(10, l))
                tmpS = str(tmp)
                lt = len(tmpS)
                if tmpS[lt - 1 - l] == '0' or tmpS[lt - 1 - l] == '1':
                    q.append([tmp // N, l + 1, lt])
            q.popleft()
        if ans == None:
            print('BRAK')
        else:
            print(ans)


if __name__ == '__main__':
    main()
