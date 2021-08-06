import sys


def main():
    N = int(sys.stdin.readline())
    digitsSize = [[0, i] for i in range(10)] # A부터 j까지 알파벳들의 자리수 값들과 알파벳 표시 idx 저장
    zeroChk = [1 for i in range(10)] # A부터 J 까지 알파벳들 중 0이 가능한 idx를 1로 표시
    usedAl = [0 for i in range(10)] # 사용된 알파벳은 1로 표시
    answer = 0
    for _ in range(N):
        getDigit(digitsSize, zeroChk)
    digitsSize.sort()
    for num in range(10):
        for i in range(10):
            size, aIdx = digitsSize[i][0], digitsSize[i][1]
            if usedAl[aIdx] == 0: # 사용 안된 알파벳일때만 진행
                if num == 0:
                    if zeroChk[aIdx]:
                        usedAl[aIdx] = 1
                        break
                else:
                    answer += (num * size)
                    usedAl[aIdx] = 1
                    break
    print(answer)


def getDigit(digitsSize, zeroChk):
    word = input()
    l = len(word)
    for i in range(l):
        c = word[l - i - 1]
        aIdx = ord(c) - 65
        digitsSize[aIdx][0] += pow(10, i)
        if i == l - 1:
            zeroChk[aIdx] = 0


if __name__ == '__main__':
    main()
