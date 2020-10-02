def main():
    N, B = map(str, input().split())
    B = int(B)
    l = len(N)
    ans = 0
    numList = [0] * l
    for i in range(l):
        num = ord(N[i])
        if num >= 65:
            numList[i] = num - 55
        else:
            numList[i] = num - 48
    for i in range(l):
        ans += numList[i] * pow(B, l - i - 1)
    print(ans)

if __name__ == "__main__":
    main()
