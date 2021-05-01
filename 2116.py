import sys


def main():
    N = int(sys.stdin.readline())
    diceList = []
    answer = 0
    for i in range(N):
        diceList.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, 7): #
        fIdx = diceList[0].index(i)
        rolling(fIdx, diceList[0]) #
        tmpAns = 0
        for j in range(1, N):
            underTop = diceList[j - 1][0] # 아래 주사위의 top의 숫자를 찾음
            bIdx = diceList[j].index(underTop) # 현재 주사위에서 bottom이 돼야하는 idx를 찾음
            rolling(bIdx, diceList[j])
        for j in range(N):
            tmpAns += max(diceList[j][1], diceList[j][2], diceList[j][3], diceList[j][4])
        if tmpAns > answer:
            answer = tmpAns
    print(answer)


def rolling(idx, dice): # idx에 있는 면을 bottom으로 만들어줌
    if idx == 0:
        dice[0], dice[5] = dice[5], dice[0]
    if idx == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]
    if idx == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[1], dice[5], dice[3], dice[2]
    if idx == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[0], dice[2], dice[5], dice[4], dice[3]
    if idx == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[0], dice[1], dice[5], dice[3], dice[4]


if __name__ == '__main__':
    main()
