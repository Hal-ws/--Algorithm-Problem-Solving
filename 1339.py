def main():
    N = int(input())
    rate = [0] * 26
    change = [0] * 26
    words = []
    ans = 0
    for i in range(26):
        rate[i] = [0, 65 + i]
    for i in range(N):
        word = input()
        getrate(word, rate)
        words.append(word)
    rate.sort(reverse=True)
    for i in range(10):
        if rate[i][0] == 0:
            break
        change[rate[i][1] - 65] = 9 - i
    for i in range(N):
        ans += changetonum(change, words[i])
    print(ans)


def getrate(word, rate):
    l = len(word)
    for i in range(1, l + 1):
        c = word[l - i]
        rate[ord(c) - 65][0] += pow(10, i - 1)


def changetonum(change, word):
    result = 0
    l = len(word)
    for i in range(l):
        cIdx = ord(word[i]) - 65
        result += change[cIdx] * pow(10, l - i - 1)
    return result


if __name__ == "__main__":
    main()
