def main():
    A, B = map(int, input().split())
    idxList, numList = [], []
    i = 1
    while 1:
        idx = (i * i - i + 2) // 2
        idxList.append(idx)
        if idx >= B:
            break
        i += 1
    li = len(idxList)
    for i in range(li - 1):
        numList += [i + 1] * (idxList[i + 1] - idxList[i])
    if B == idxList[li - 1]:
        numList.append(li)
    print(sum(numList[A - 1:B]))


if __name__ == "__main__":
    main()
