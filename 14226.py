def main():
    S = int(input())
    timeresult = [[[2, 1]], [[3, 1]]] ## 2, 3초에 생기는 경우의수
    time = 4
    if S == 2:
        print(2)
    else:
        endflag = 0
        while 1:
            first = timeresult[0]
            second = timeresult[1]
            temp = []
            l1 = len(first)
            l2 = len(second)
            for i in range(l1):
                if first[i][0] * 2 == S:
                    endflag = 1
                    break
                temp.append([first[i][0] * 2, first[i][0]])
            for i in range(l2):
                if second[i][0] + second[i][1] == S:
                    endflag = 1
                    break
                temp.append([second[i][0] + second[i][1], second[i][1]])
                if second[i][0] - 1 > 4:
                    if second[i][0] - 1 == S:
                        endflag = 1
                        break
                    temp.append([second[i][0] - 1, second[i][1]])
            if endflag:
                break
            timeresult[0] = timeresult[1]
            timeresult[1] = temp
            time += 1
        print(time)


if __name__ == "__main__":
    main()
