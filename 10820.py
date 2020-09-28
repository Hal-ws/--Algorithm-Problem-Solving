while True:
    try:
        words = input()
    except EOFError:
        break
    lw = len(words)
    cntN, cntSpace, cntLarge, cntSmall = 0, 0, 0, 0
    for j in range(lw):
        if words[j] == ' ':
            cntSpace += 1
        elif ord(words[j]) >= 97:
            cntSmall += 1
        elif ord(words[j]) >= 65:
            cntLarge += 1
        else:
            cntN += 1
    print('%s %s %s %s' % (cntSmall, cntLarge, cntN, cntSpace))
