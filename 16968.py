def main():
    form = input()
    cc = 0 #c가 연속해서 이어질때
    dc = 0 #d가 연속해서 이어질때
    ans = 1
    for w in form:
        if w == 'c':
            if cc: #앞에 문자가 붙어있을때
                ans *= 25
            else:
                ans *= 26
            cc = 1
            dc = 0
        if w == 'd':
            if dc: #앞에 숫자가 붙어있을때
                ans *= 9
            else:
                ans *= 10
            dc = 1
            cc = 0
    print(ans)


if __name__ == '__main__':
    main()
