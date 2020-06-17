N = int(input())

def checkpossible(newQueen, queens): ## newQueen의 좌표값을 받음
    for i in range(len(queens)):
        if queens[i] == newQueen[1] or newQueen[0] - queens.index(queens[i]) == newQueen[1] - queens[i]:
            return False
    return True

def path(queens): #queens는 이미 queen들이 배치된 좌표를 리스트로 입력, 0행부터 순서대로 열의 좌표만 입력한다
    if len(queens) == N:
        return True
    for i in range(N): ## 새 queen을 배치
        flag = 1
        newPos = [len(queens), i]
        if checkpossible(newPos, queens) == False:
            flag = 0
            break
cnt = 0
