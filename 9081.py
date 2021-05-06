def main():
    T = int(input())
    for _ in range(T):
        word = list(input())
        for i in range(len(word) - 1, -1, -1):
            minVal = 'Z' # word[i]보다 큰 값 중 제일 작은 값
            minIdx = None
            for j in range(i + 1, len(word)):
                if word[i] < word[j] and word[j] <= minVal:
                    minVal = word[j]
                    minIdx = j
            if minIdx != None:
                word[i], word[minIdx] = word[minIdx], word[i]
                tmpList = [word[j] for j in range(i + 1, len(word))]
                tmpList.sort()
                for j in range(len(tmpList)):
                    word[i + j + 1] = tmpList[j]
                break
        for i in range(len(word)):
            print(word[i], end='')
        print()


if __name__ == '__main__':
    main()
