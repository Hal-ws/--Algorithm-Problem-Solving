import sys
from itertools import product


def main():
    global numBoard, digitSum
    N = int(sys.stdin.readline())
    w = 4 * N - 1
    bCases = list(product(['.', '#'], repeat=15))# 가능한 모든 boards의 case
    numBoard = ["####.##.##.####", "..#..#..#..#..#", "###..#####..###", "###..####..####", "#.##.####..#..#",
                "####..###..####", "####..####.####", "###..#..#..#..#", "####.#####.####", "####.####..####"]
    inputBoard = []
    for _ in range(5):
        inputBoard.append(sys.stdin.readline()[:w])
    digitSum = {} # key에 따른 digit의 값을 다 더해줌
    digitCnt = {} # key에 따른 값의 수를 다 곱해줌
    ans = 0
    cnt = 0 # 가능한 수
    for case in bCases:
        chk(case) #현재 case에서 가능한 숫자를 digitSum에 추가한다
    # 하나라도 가능한 수를 못찾으면 ans = -1
    for j in range(0, w, 4):
        digit = N - 1 - (j // 3)
        key = ''
        print('digit: %s' %digit)
        for i in range(5):
            key += (inputBoard[i][j] + inputBoard[i][j + 1] + inputBoard[i][j + 2])
        if digitSum[key] == -1:
            ans = -1
            break
        else:
            ans += digitSum[key] * pow(10, digit)
    if ans == -1:
        print(ans)
    else:
        print(ans / cnt)


def chk(case):
    global numBoard, digitSum
    key = '' #해당 key로 만들수 있는거 확인
    for i in range(15):
        key += case[i]
    digitSum[key] = -1
    for i in range(10): #0~10까지 가능한것 확인
        std = numBoard[i]
        flag = 1 # case가 std가 될 수 있는지 확인
        for j in range(15):
            if std[j] == '.' and key[j] == '#': # 꺼져 있어야 하는데 켜져있음
                flag = 0
                break
        if flag:
            if digitSum[key] == -1:
                digitSum[key] = i
            else:
                digitSum[key] += i


if __name__ == '__main__':
    main()
