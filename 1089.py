import sys
from itertools import product


def main():
    global numBoard, digitSum, digitCnt
    N = int(sys.stdin.readline())
    w = 4 * N - 1
    bCases = list(product(['.', '#'], repeat=15))# 가능한 모든 boards의 case
    numBoard = ["####.##.##.####", "..#..#..#..#..#", "###..#####..###", "###..####..####", "#.##.####..#..#",
                "####..###..####", "####..####.####", "###..#..#..#..#", "####.#####.####", "####.####..####"]
    inputBoard = []
    for _ in range(5):
        inputBoard.append(sys.stdin.readline()[:w])
    digitSum = {} # key에 따른 digit의 값을 다 더해줌
    digitCnt = {} # key에 따른 값의 수를 다 구해줌
    digitNum = [] # 각 자릿수의 합
    cntList = [] # 각 자릿수의 경우의 수
    for case in bCases:
        chk(case) #현재 case에서 가능한 숫자를 digitSum에 추가한다
    # 하나라도 가능한 수를 못찾으면 -1출력후 return
    for j in range(0, w, 4):
        key = ''
        for i in range(5):
            key += (inputBoard[i][j] + inputBoard[i][j + 1] + inputBoard[i][j + 2])
        if digitCnt[key] == 0:
            print(-1)
            return
        else:
            digitNum.append(digitSum[key])
            cntList.append(digitCnt[key])
    result = 0
    divVal = 1
    if N == 1:
        print(digitNum[0] / cntList[0])
    else:
        for i in range(N):
            mulVal = 1
            for j in range(N):
                if i != j:
                    mulVal *= cntList[j]
            result += digitNum[i] * pow(10, N - i - 1) * mulVal
            divVal *= cntList[i]
        print(result / divVal)


def chk(case):
    global numBoard, digitSum, digitCnt
    key = '' #해당 key로 만들수 있는거 확인
    for i in range(15):
        key += case[i]
    digitSum[key] = 0
    digitCnt[key] = 0
    for i in range(10): # 0~10까지 가능한것 확인
        std = numBoard[i]
        flag = 1 # case가 std가 될 수 있는지 확인
        for j in range(15):
            if std[j] == '.' and key[j] == '#': # 꺼져 있어야 하는데 켜져있음
                flag = 0
                break
        if flag:
            digitSum[key] += i
            digitCnt[key] += 1


if __name__ == '__main__':
    main()
