N = int(input())

numbers = list(map(int, input().split()))
flag = 0
if N >= 3:
    if numbers[1] - numbers[0] == 0:
        a = 1
        b = 0
    else:
        if (numbers[2] - numbers[1]) % (numbers[1] - numbers[0]) != 0:
            flag = 1
        if flag == 0:
            a = (numbers[2] - numbers[1]) // (numbers[1] - numbers[0])
            b = numbers[1] - numbers[0] * a
    if flag == 0:
        for i in range(2, N):
            if numbers[i] != (numbers[i - 1] * a + b):
                flag = 1
                break

elif N == 1:
    flag = -1
elif N == 2:
    if numbers[0] == numbers[1]:
        a = 1
        b = 0
    else:
        flag = -1

if flag == 0:
    print(numbers[N - 1] * a + b)
elif flag == -1:
    print('A')
else:
    print('B')
