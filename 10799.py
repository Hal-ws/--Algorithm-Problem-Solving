def Main():
    a = input()
    la = len(a)
    platestack = 0
    ans = 0
    for i in range(la):
        if a[i] == "(":
            platestack += 1
        else:
            platestack -= 1
            if a[i - 1] == "(":
                ans += platestack
            else:
                ans += 1
    print(ans)


if __name__ == "__main__":
    Main()
