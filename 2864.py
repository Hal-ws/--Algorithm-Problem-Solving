import sys
a, b = map(int, sys.stdin.readline().split())

tempA = str(a)
for i in range(len(tempA)):
    if tempA[i] == '6':
        a -= pow(10, len(tempA) - i - 1)
tempB = str(b)
for i in range(len(tempB)):
    if tempB[i] == '6':
        b -= pow(10, len(tempB) - i - 1)

min = a + b
tempA = str(a)

for i in range(len(tempA)):
    if tempA[i] == '5':
        a += pow(10, len(tempA) - i - 1)
tempB = str(b)
for i in range(len(tempB)):
    if tempB[i] == '5':
        b += pow(10, len(tempB) - i - 1)
max = a + b

print(str(min) + ' ' + str(max))
