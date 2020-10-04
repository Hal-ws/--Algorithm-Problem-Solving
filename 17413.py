def main():
    sentence = input()
    ans = ''
    ls = len(sentence)
    i = 0
    while i < ls:
        if sentence[i] == '<':
            ans += sentence[i]
            j = i + 1
            while True:
                ans += sentence[j]
                if sentence[j] == '>':
                    i = j + 1
                    break
                j += 1
        elif sentence[i] == ' ':
            ans += ' '
            i += 1
        else:
            j = i + 1
            jump = 0
            while j < ls:
                if sentence[j] == '<':
                    break
                if sentence[j] == ' ':
                    jump = 1
                    break
                j += 1
            ans += reverse(sentence[i:j]) + ' ' * jump
            if j == ls or sentence[j] == '<':
                i = j
            else:
                i = j + 1
    print(ans)


def reverse(word):
    lw = len(word)
    reversed = ''
    for i in range(lw - 1, -1, -1):
        reversed += word[i]
    return reversed


if __name__ == "__main__":
    main()
