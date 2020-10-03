from itertools import combinations


def main():
    L, C = map(int, input().split())
    codes = list(map(str, input().split()))
    vowel = []
    consonant = []
    for i in range(C):
        if codes[i] == 'a' or codes[i] == 'e' or codes[i] == 'i' or codes[i] == 'o' or codes[i] == 'u':
            vowel.append(codes[i])
        else:
            consonant.append(codes[i])
    vowel.sort()
    consonant.sort()
    l = len(vowel)
    passwordList = []
    for i in range(1, l + 1): # i
        if L - i < 2:
            break
        passwordList += makingpassword(i, vowel, consonant, L)
    lp = len(passwordList)
    passwordList.sort()
    for i in range(lp):
        for j in range(L):
            print(passwordList[i][j], end = '')
        print()
    return 0


def makingpassword(n, vowel, consonant, L): # n: password에 있는 모음의 수
    vowelList = list(combinations(vowel, n))
    consList = list(combinations(consonant, L - n))
    lv, lc = len(vowelList), len(consList)
    password = []
    for i in range(lv):
        for j in range(lc):
            temp = list(vowelList[i] + consList[j])
            temp.sort()
            password.append(temp)
    return password


if __name__ == "__main__":
    main()

