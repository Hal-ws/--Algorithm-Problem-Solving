import sys
from itertools import combinations


def main():
    global N, nList, ans, iList
    ans = - 1 * pow(2, 31)
    N = int(sys.stdin.readline())
    iList = [i * 2 for i in range(N // 2 + 1)]
    nList = list(sys.stdin.readline()[:N])
    for i in range(N):
        if i % 2 == 0:
            nList[i] = int(nList[i])
    if N == 1:
        print(nList[0])
        return
    for i in range(N):
        if i % 2 == 0:
            nList[i] = int(nList[i])
    for i in range(2, N // 2 + 2, 2):
        getresult(i)
    print(ans)


def getresult(cnt): # 괄호의 개수
    global N, nList, ans, iList
    cases = list(combinations(iList, cnt))
    for case in cases:
        pList = [0] * N
        for i in range(len(case)):
            if i % 2 == 0: #짝수일때, 괄호 start
                pList[case[i]] = 's'
            else:
                pList[case[i]] = 'e'
        i = 0
        flag = 1
        while i < N:
            if pList[i] == 's': # 괄호 시작
                sIdx = i
                for j in range(sIdx + 1, N):
                    if pList[j] == 'e':
                        eIdx = j
                        break
                if eIdx - sIdx > 2:
                    flag = 0
                    break
                if sIdx == 0: #시작하자마자 괄호에 있는경우
                    val = calculation(sIdx, eIdx)
                else:
                    if nList[sIdx - 1] == '+':
                        val += calculation(sIdx, eIdx)
                    if nList[sIdx - 1] == '-':
                        val -= calculation(sIdx, eIdx)
                    if nList[sIdx - 1] == '*':
                        val *= calculation(sIdx, eIdx)
                i = eIdx + 2
            else:
                if i == 0:
                    val = nList[i]
                else:
                    if nList[i - 1] == '+':
                        val += nList[i]
                    if nList[i - 1] == '-':
                        val -= nList[i]
                    if nList[i - 1] == '*':
                        val *= nList[i]
                i += 2
        if val >= ans and flag:
            ans = val


def calculation(sIdx, eIdx):
    global N, nList, ans
    val = nList[sIdx]
    for i in range(sIdx + 2, eIdx + 1, 2):
        t = nList[i]
        if nList[i - 1] == '+':
            val += t
        if nList[i - 1] == '-':
            val -= t
        if nList[i - 1] == '*':
            val *= t
    return val


if __name__ == '__main__':
    main()
