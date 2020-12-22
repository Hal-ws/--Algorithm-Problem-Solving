from itertools import combinations, permutations


def main():
    word = []
    for i in range(6):
        word.append(input())
    wordIdx = [0, 1, 2, 3, 4, 5]
    cases = list(combinations(wordIdx, 3)) #가로를 뽑음
    answer = []
    for case in cases:
        assemble(case, word, answer)
    if len(answer) == 0:
        print(0)
    else:
        answer = sorted(answer)[0]
        for i in range(3):
            print(answer[i])


def assemble(case, word, answer):
    vertical = []
    for i in range(6):
        if i not in case:
            vertical.append(i)
    vPerm = list(permutations([0, 1, 2], 3))
    pPerm = list(permutations([0, 1, 2], 3))
    for vcase in vPerm:
        for pcase in pPerm:
            flag = 1 #이 케이스일때 가능한지 확인
            tmpP = [word[case[pcase[0]]], word[case[pcase[1]]], word[case[pcase[2]]]]
            tmpV = ['', '', '']
            for j in range(3):
                tmpW = word[vertical[vcase[j]]]
                for i in range(3):
                    tmpV[i] = tmpV[i] + tmpW[i]
            for i in range(3):
                for j in range(3):
                    if tmpP[i][j] != tmpV[i][j]:
                        flag = 0
            if flag:
                answer.append(tmpP)


if __name__ == '__main__':
    main()

