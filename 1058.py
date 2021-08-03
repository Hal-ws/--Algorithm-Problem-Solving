import sys


def main():
    N = int(sys.stdin.readline())
    matrix = []
    for _ in range(N):
        matrix.append(list(sys.stdin.readline()[:N]))
    answer = 0
    for i in range(N):
        tmp = getCnt(matrix, i, N)
        if tmp >= answer:
            answer = tmp
    print(answer)


def getCnt(matrix, idx, N): # idx번째의 2-친구값을 구함
    fChk = [0 for j in range(N)]
    fList = []
    for j in range(N):
        if matrix[idx][j] == 'Y':
            fChk[j] = 1
            fList.append(j)
    for i in range(len(fList)):
        f1 = fList[i]
        for j in range(N):
            if j != idx and matrix[f1][j] == 'Y':
                fChk[j] = 1
    return sum(fChk)


if __name__ == '__main__':
    main()
