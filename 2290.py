def main():
    s, n = map(str, input().split())
    ln = len(n)
    s= int(s)
    ans = [0] * ln
    for i in range(ln):
        ans[i] = getnum(s, int(n[i]))
    for i in range(2 * s + 3):
        for j in range(ln):
            print(ans[j][i], end=' ')
        print()


def getnum(s, n):
    word = [0 for i in range(2 * s + 3)]
    # 첫줄 그림
    if n == 1 or n == 4:
        word[0] = ' ' * (s + 2)
    else:
        word[0] = ' ' + '-' * s + ' '
    # 두번째줄~중간 전줄까지 그림
    if n == 1 or n == 2 or n == 3 or n ==7:
        for i in range(1, s + 1):
            word[i] = ' ' * (s + 1) + '|'
    elif n == 5 or n == 6:
        for i in range(1, s + 1):
            word[i] = '|' + ' ' * (s + 1)
    else:
        for i in range(1, s + 1):
            word[i] = '|' + ' ' * s + '|'
    # 가운데줄
    if n == 1 or n == 7 or n == 0:
        word[s + 1] = ' ' * (s + 2)
    else:
        word[s + 1] = ' ' + '-' * s + ' '
    # ~마지막줄 전까지
    if n == 1 or n == 3 or n == 4 or n == 5 or n == 7 or n == 9:
        for i in range(s + 2, 2 * s + 2):
            word[i] = ' ' * (s + 1) + '|'
    elif n == 2:
        for i in range(s + 2, 2 * s + 2):
            word[i] = '|' + ' ' * (s + 1)
    else:
        for i in range(s + 2, 2 * s + 2):
            word[i] = '|' + ' ' * s + '|'
    # 마지막줄
    if n == 1 or n == 4 or n == 7:
        word[2 * s + 2] = ' ' * (s + 2)
    else:
        word[2 * s + 2] = ' ' + '-' * s + ' '
    return word


if __name__ == "__main__":
    main()
