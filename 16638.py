import sys
from itertools import combinations


def main():
    global N
    N = int(sys.stdin.readline())
    expression = sys.stdin.readline()[:N]
    nList = [i for i in range(0, N, 2)] # expression에서 숫자가 있는 idx를 나타내는 리스트
    ans = -1 * pow(2, 31)
    if N == 1:
        print(expression[0])
    else:
        for i in range(2, N, 2):
            cases = list(combinations(nList, i))
            for case in cases:
                pFlag = 1
                for i in range(0, len(case), 2):
                    if case[i + 1] - case[i] > 2:
                        pFlag = 0
                        break
                if pFlag:
                    tmp = calculation(changePostfix(makingME(expression, case)))
                    if ans < tmp:
                        ans = tmp
        print(ans)


def calculation(postfix):
    stack = []
    for c in postfix:
        if c == '+':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 + v2)
        elif c == '-':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v2 - v1)
        elif c == '*':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 * v2)
        else:
            stack.append(int(c))
    return stack[0]


def makingME(expression, case):  # 수식을 만들어줌
    N = len(expression)
    result = ''
    for i in range(case[0]):
        result += expression[i]
    for i in range(len(case)):
        pIdx = case[i]  # 괄호가 있는 위치
        if i % 2 == 0:  # (를 추가해야 할 때
            result += '('
            for j in range(pIdx, case[i + 1] + 1):
                result += expression[j]
        else:
            result += ')'
            if i < len(case) - 1:  # 마지막 괄호가 아닐 시
                for j in range(pIdx + 1, case[i + 1]):
                    result += expression[j]
            else:
                for j in range(pIdx + 1, N):
                    result += expression[j]
    return result


def changePostfix(me):
    stack = []
    result = ''
    for c in me:
        if c == '(':
            stack.append(c)
        elif c == ')':
            for i in range(len(stack) - 1, -1, -1):
                top = stack.pop()
                if top == '(':
                    break
                else:
                    result += top
        elif c == '+' or c == '-':
            while len(stack) > 0:
                top = stack.pop()
                if top != '(' and top != ')':
                    result += top
                else:
                    stack.append(top)
                    break
            stack.append(c)
        elif c == '*':
            while len(stack) > 0:
                top = stack.pop()
                if top == '*':
                    result += top
                else:
                    stack.append(top)
                    break
            stack.append(c)
        else:
            result += c
    while len(stack) > 0:
        result += stack.pop()
    return result


if __name__ == '__main__':
    main()
