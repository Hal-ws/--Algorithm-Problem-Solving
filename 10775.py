import sys


def main():
    global emptyGate
    G = int(sys.stdin.readline())
    emptyGate = [i for i in range(G + 1)] # emptyGate[i]: i번 이하의 gate 비어있는 gate 중 제일 큰 값 (값이 0이면 다 찬거임)
    P = int(sys.stdin.readline())
    cnt = 0
    for i in range(P):
        pNum = int(sys.stdin.readline())
        dockingG = find(pNum)
        if dockingG != 0: # 도킹 가능한 Gate가 남아있음
            emptyGate[dockingG] = find(dockingG - 1) #도킹했으니 더 작은 gate의 값을 받아온다
            cnt += 1
        else:
            break
    print(cnt)


def find(pNum):
    global emptyGate
    if emptyGate[pNum] == 0:
        return 0
    if emptyGate[pNum] == pNum:
        return pNum
    emptyGate[pNum] = find(emptyGate[pNum])
    return emptyGate[pNum]


if __name__ == '__main__':
    main()
