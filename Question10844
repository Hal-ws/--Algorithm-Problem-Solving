N = int(input())

cases = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]] ## N이 2일때 값

for i in range(N - 2):
    temp = [0] * 10
    for j in range(10):
        if j == 0:
            temp[j] = cases[i + 1][1] % 1000000000
        elif j == 9:
            temp[j] = cases[i + 1][8] % 1000000000
        else:
            temp[j] = (cases[i + 1][j - 1] % 1000000000 + cases[i + 1][j + 1] % 1000000000) % 1000000000
    cases.append(temp)

if N == 1:
    print(9)
else:
    print(sum(cases[N - 1][1:]) % 1000000000)
