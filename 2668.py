import sys

def main():
    N = int(sys.stdin.readline())
    numList = [0]
    cycle = [0 for i in range(N + 1)]
    for i in range(N):
        numList.append(int(sys.stdin.readline()))
    ansList = []
    for i in range(1, N + 1):
        visit = set()
        visit.add(i)
        if cycle[i] == 0:
            dfs(i, numList, cycle, visit)
    for i in range(1, N + 1):
        if cycle[i]:
            ansList.append(i)
    print(len(ansList))
    for i in range(len(ansList)):
        print(ansList[i])


def dfs(num, numList, cycle, visit):
    nxtNum = numList[num] # 다음 num 저장
    if cycle[nxtNum]:
        return 0
    if nxtNum in visit: # cycle 성립
        cycle[num] = 1
        if nxtNum == num:
            return 0
        return nxtNum # cycle을 시작하는 idx를 return
    visit.add(nxtNum) # 다음 num을 방문한 곳에 추가
    result = dfs(nxtNum, numList, cycle, visit)
    if result == 0:
        return 0
    else:
        cycle[num] = 1
        if result == num: # 사이클 끝날때
            return 0
        else:
            return result


if __name__ == "__main__":
    main()
