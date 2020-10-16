def main():
    N = int(input())
    ansList = [0, 1] ## 0으로 끝나는 이친수 개수, 1로 끝나는 이친수 개수
    for i in range(N - 1):
        temp0 = ansList[0]
        temp1 = ansList[1]
        ansList[0] = temp0 + temp1
        ansList[1] = temp0
    print(sum(ansList))


if __name__ == "__main__":
    main()
