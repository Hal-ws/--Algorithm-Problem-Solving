def Main():
    sentence = input()
    ls = len(sentence)
    ans = ''
    for i in range(ls):
        if sentence[i] == ' ':
            ans = ans + sentence[i]
        else:
            asci = ord(sentence[i])
            if asci <= 57:
                ans = ans + sentence[i]
            else:
                ans = ans + encoding(asci)
    print(ans)


def encoding(asci):
    if asci >= 97:
        asci += 13
        if asci > 122:
            asci -= 26
    if asci <= 90:
        asci += 13
        if asci > 90:
            asci -= 26
    word = chr(asci)
    return word


if __name__ == "__main__":
    Main()
