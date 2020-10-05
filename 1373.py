def Main():
    N = input()
    lN = len(N)
    minimum = ["0", "1", "10", '11', '100', '101', '110', '111']
    if lN <= 3:
        print(minimum.index(N))
    else:
        ans = ''
        startIdx = lN - (3 * (lN // 3))
        i = startIdx
        while i <= lN - 3:
            if N[i] == '0' and N[i + 1] == '0' and N[i + 2] == '0':
                ans = ans + '0'
            if N[i] == '0' and N[i + 1] == '0' and N[i + 2] == '1':
                ans = ans + '1'
            if N[i] == '0' and N[i + 1] == '1' and N[i + 2] == '0':
                ans = ans + '2'
            if N[i] == '0' and N[i + 1] == '1' and N[i + 2] == '1':
                ans = ans + '3'
            if N[i] == '1' and N[i + 1] == '0' and N[i + 2] == '0':
                ans = ans + '4'
            if N[i] == '1' and N[i + 1] == '0' and N[i + 2] == '1':
                ans = ans + '5'
            if N[i] == '1' and N[i + 1] == '1' and N[i + 2] == '0':
                ans = ans + '6'
            if N[i] == '1' and N[i + 1] == '1' and N[i + 2] == '1':
                ans = ans + '7'
            i += 3
        if startIdx == 1:
            ans = '1' + ans
        if startIdx == 2:
            if N[1] == '0':
                ans = '2' + ans
            if N[1] == '1':
                ans = '3' + ans
        print(ans)


if __name__ == "__main__":
    Main()
