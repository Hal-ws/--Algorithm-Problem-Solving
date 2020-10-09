N = int(input())

def getCount(number):
    cnt = 0
    number = str(number)
    for i in range(len(number)):
        if number[i] == '3' or number[i] == '6' or number[i] == '9':
            cnt += 1
    return cnt

ans = 0
for i in range(1, N + 1):
    ans += getCount(i)
print(ans)
