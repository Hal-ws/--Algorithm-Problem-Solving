def main():
    N, M = map(int, input().split())
    wordList = [[] for j in range(26)] # a, b, c로 시작하는 애들을 모음
    cnt = 0
    for i in range(N):
        word = input()
        wordList[ord(word[0]) - 97].append([word, len(word)])
    for i in range(M):
        tmp = input()
        l1 = len(tmp)
        s = ord(tmp[0]) - 97
        for t in wordList[s]:
            w, l2 = t[0], t[1]
            if l1 <= l2 and tmp == w[:l1]:#
                cnt += 1
                break
    print(cnt)


if __name__ == '__main__':
    main()
