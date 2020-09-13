num = sorted(list(map(int, input().split())))
if max(num) == min(num):
    print(10000 + num[0] * 1000)
elif num[0] != num[1] != num[2]:
    print(100 * num[2])
else:
    if num[0] == num[1]:
        print(1000 + num[0] * 100)
    else:
        print(1000 + num[2] * 100)
