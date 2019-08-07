N, M = map(int, input().split())
i = 0
inputBoard = []
while(i < N):                  ## 주어진 값으로 비교
    inputBoard.append(input())
    i += 1

whiteBoard = ['WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW']

def countChange(inputBoard, whiteBoard): ## white 체스판과 비교해서 틀린게 몇개 있는지 확인
    cnt = 0
    i = 0
    while (i < 8):
        j = 0
        while (j < 8):
            if (inputBoard[i][j] != whiteBoard[i][j]):
                cnt += 1
            j += 1
        i += 1
    return cnt

def sliceBoard(inputBoard, i, j):
    slicedBoard = []
    k = i + 8
    while(i < k):
        slicedBoard.append(inputBoard[i][j:j + 8])
        i += 1
    return slicedBoard

anslist = []
i = 0
while(i <= N - 8):
    j = 0
    while(j <= M - 8):
        testBoard = sliceBoard(inputBoard, i, j)
        if(countChange(testBoard, whiteBoard) <= 32):
            anslist.append(countChange(testBoard, whiteBoard))
        else:
            anslist.append(64 - countChange(testBoard, whiteBoard))
        j += 1
    i += 1

print(min(anslist))
