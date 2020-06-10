import sys
import math

def getdivisers(num):
    divisers = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisers.append(i)
            if i != num // i:
                divisers.append(num // i)
    divisers = sorted(divisers[1:])
    return divisers

N = int(sys.stdin.readline())

numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers = sorted(numbers)
divisers = getdivisers(numbers[len(numbers) - 1] - numbers[0])

ans = []
compare = list(map(int, sys.stdin.readline().split()))
for i in range(len(divisers)):
    std = numbers[0] % divisers[i]
    flag = 0
    for j in range(1, len(numbers)):
        if numbers[j] % divisers[i] != std:
            flag = 1
            break
    if flag == 0:
        ans.append(divisers[i])

for i in range(len(ans)):
    print(ans[i], end=' ')
