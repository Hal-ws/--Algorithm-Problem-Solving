import math, itertools

N = int(input())
numList = list(map(int, input().split()))
signCounts= list(map(int , input().split()))
signs = '+' * signCounts[0]
signs += '-' * signCounts[1]
signs += '*' * signCounts[2]
signs += '/' * signCounts[3]
signCases = list(itertools.permutations(signs, len(signs)))

formula = []
formula.append(numList[0])
for i in range(len(numList) - 1):
    formula.append(0)
    formula.append(numList[i + 1])

ansList = []
for i in range(len(signCases)):
    for j in range(N - 1):
        formula[2*j + 1] = signCases[i][j]
    temp = formula[0]
    print(formula)
    for k in range(N - 1):
        if formula[2 * k + 1] == '+':
            temp += formula[2 * k + 2]
        elif formula[2 * k + 1] == '-':
            temp -= formula[2 * k + 2]
        elif formula[2 * k + 1] == '*':
            temp *= formula[2 * k + 2]
        else:
            if temp < 0:
                temp *= (-1)
                temp //= formula[2 * k + 2]
                temp *= (-1)
            else:
                temp //= formula[2 * k + 2]
    ansList.append(temp)

print(max(ansList))
print(min(ansList))
