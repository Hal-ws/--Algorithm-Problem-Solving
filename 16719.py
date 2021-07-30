def main():
    word = list(input())
    l = len(word)
    used = [0 for i in range(l)]
    for _ in range(l):
        print(findfirst(word, used, l))


def findfirst(word, used, l):
    candidates = []
    for i in range(l):
        if used[i] == 0: #안쓴거일때
            # candidates에 word를 만들어줌
            tmpWord = ''
            used[i] = 1
            for j in range(l):
                if used[j]:
                    tmpWord += word[j]
            used[i] = 0
            candidates.append([tmpWord, i]) # i번째 문자를 새로 고름
    candidates.sort()
    result = candidates[0][0]
    used[candidates[0][1]] = 1
    return result


if __name__ == "__main__":
    main()
