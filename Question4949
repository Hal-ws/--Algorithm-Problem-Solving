import sys
std = '()[]'

def getIdx(paren, stack):
    delIdx = None
    length = len(stack)
    for i in range(1, length + 1):
        if stack[length - i] == paren:
            delIdx = length - i
            break
    return delIdx

while 1:
    line = sys.stdin.readline()
    line = line[:len(line) - 1]
    if line == '.':
        break
    parentheses = []
    for i in range(len(line)):
        if line[i] in std:
            parentheses.append(line[i])
    stack = []
    flag = 1
    for i in range(len(parentheses)):
        if parentheses[i] == '(' or parentheses[i] == '[':
            stack.append(parentheses[i])
        elif parentheses[i] == ')':
            delIdx = getIdx('(', stack)
            if delIdx == None:
                flag = -1
                break
            if getIdx('[', stack[delIdx:]) != None:
                flag = -1
                break
            del stack[getIdx('(', stack)]
        elif parentheses[i] == ']':
            delIdx = getIdx('[', stack)
            if delIdx == None:
                flag = -1
                break
            if getIdx('(', stack[delIdx:]) != None:
                flag = -1
                break
            del stack[getIdx('[', stack)]
    if flag == -1 or len(stack) != 0:
        print('no')
    else:
        print('yes')
