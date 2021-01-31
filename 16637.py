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
    print(nList)
    for i in range(N):
        if i % 2 == 0:
            nList[i] = int(nList[i])
    for i in range(2, N // 2 + 2, 2):
        getresult(i)



def getresult(cnt): # 괄호의 개수
    global N, nList, ans, iList
    cases = list(combinations(iList, cnt))
    for case in cases:
        pList = [0] * N
        print('case: %s' %list(case))
        for i in range(len(case)):
            if i % 2 == 0: #짝수일때, 괄호 start
                pList[case[i]] = 's'
            else:
                pList[case[i]] = 'e'
        print(pList)
        calculation(pList)


def calculation(pList):
    global N, nList, ans
    i = 0
    val = 0
    while i < N:
        
        i += 2




if __name__ == '__main__':
    main()
