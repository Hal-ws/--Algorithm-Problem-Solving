def main():
    number = input()
    ln = len(number)
    ans = 0
    for i in range(ln):
        if number[i] != "A" and number[i] != "B" and number[i] != "C" and number[i] != "D" and number[i] != "E" and number[i] != "F":
            ans += int(number[i]) * pow(16, ln - i - 1)
        else:
            ans += (ord(number[i]) - 55) * pow(16, ln - i - 1)
    print(ans)


if __name__ == "__main__":
    main()
