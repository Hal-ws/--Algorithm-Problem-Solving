n = int(input())
b = list(map(int, input().split()))

M = max(b)
i = 0
sum = 0
while (i < len(b)):
    b[i] = (b[i]/M)*100 ## 값 수정
    sum = sum + b[i]
    i += 1
print(sum / n)
