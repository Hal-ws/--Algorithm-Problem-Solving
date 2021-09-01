def main():
    word = input()
    if word == '0':
        print('W')
        return
    ansList = []
    tmp = ''
    for i in range(len(word)):
        if word[i] == '+' or word[i] == '-':
            ansList.append(tmp)
            ansList.append(word[i])
            tmp = ''
        else:
            tmp += word[i]
    ansList.append(tmp)
    ansList.append('+')
    ansList.append('W')
    for i in range(len(ansList)):
        if ansList[i] != '+' and ansList[i] != '-' and len(ansList[i]) > 0:
            sIdx = i
            break
    for i in range(sIdx, len(ansList) - 1, 2):
        ansList[i] = transform(ansList[i])
    i = sIdx
    while i < len(ansList):
        if ansList[i] != '0':
            if i > 0:
                print(ansList[i - 1], end='')
            print(ansList[i], end='')
        i += 2


def transform(value):
    if value == '0':
        return '0'
    xCnt = value.count('x')
    if xCnt == 0:
        if value == '1':
            return 'x'
        return value + 'x'
    num = int(value[:len(value) - xCnt]) // 2
    if num == 1:
        return 'x' * (xCnt + 1)
    else:
        return str(num) + 'x' * (xCnt + 1)
    return str(num // 2) + 'x' * (xCnt + 1)


if __name__ == "__main__":
    main()
