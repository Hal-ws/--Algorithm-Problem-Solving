def main():
    tans = int(input())
    rightAns = [1] * 65
    for i in range(1, 65):
        rightAns[i] = rightAns[i - 1] * 2
    wrongAns = [1] * 65
    for i in range(1, 65):
        wrongAns[i] = (rightAns[i - 1] * 2 - 1) * pow(2, 64 - i)
    print(wrongAns.index(tans))


if __name__ == '__main__':
    main()
