def main():
    word = input()
    lw = len(word)
    flag = 1
    for i in range(lw // 2):
        if word[i] != word[lw - i - 1]:
            flag = 0
            break
    print(flag)


if __name__ == "__main__":
    main()
