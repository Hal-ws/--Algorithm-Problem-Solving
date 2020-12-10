def main():
    N, K = map(int, input().split())
    getangle = list(map(int, input().split()))
    l = len(getangle)
    target = list(map(int, input().split()))
    chk = [0] * 360
    for i in range(l):
        chk[getangle[i]] = 1
    while 1:
        flag = 0
        for i in range(l):
            for j in range(i, l):
                newangle = (getangle[i] + getangle[j]) % 360
                if chk[newangle] == 0:
                    getangle.append(newangle)
                    chk[newangle] = 1
                    flag = 1
                    l += 1
                newangle = (getangle[i] - getangle[j]) % 360
                if chk[newangle] == 0:
                    getangle.append(newangle)
                    chk[newangle] = 1
                    flag = 1
                    l += 1
                newangle = (getangle[j] - getangle[i]) % 360
                if chk[newangle] == 0:
                    getangle.append(newangle)
                    chk[newangle] = 1
                    flag = 1
                    l += 1
        if flag == 0: #새로 추가된게 없음
            break
    for angle in target:
        if chk[angle]:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
