def main():
    time = list(map(int, input().split(':')))
    HHMMSS = []
    MMSS = []
    for num in time:
        if 0 < num <= 12:
            HHMMSS.append(num)
        elif num < 60:
            MMSS.append(num)
    if len(HHMMSS) == 0: #표현할수 있는 시가 없음
        answer = 0
    if len(HHMMSS) == 1:
        if len(MMSS) == 1 or len(MMSS) == 0: #분, 초를 나타낼게 부족함
            answer = 0
        else:
            answer = 2
    if len(HHMMSS) == 2:
        if len(MMSS) != 1:
            answer = 0
        else:
            answer = 4
    if len(HHMMSS) == 3:
        answer = 6
    print(answer)


if __name__ == '__main__':
    main()
