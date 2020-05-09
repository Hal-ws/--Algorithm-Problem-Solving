import sys

n = int(sys.stdin.readline())
number = [0] * n
for i in range(n):
    number[i] = int(sys.stdin.readline())
waiting = [0] * n
for i in range(n):
    waiting[i] = i + 1

i = 0
stack = []
ans = ''
flag = 0
for i in range(n):
    lenStack = len(stack)
    if lenStack == 0:
        for j in range(waiting.index(number[i])):
            stack.append(waiting[j])
        ans = ans + '+' * (waiting.index(number[i]) + 1) + '-'
        waiting = waiting[waiting.index(number[i]) + 1:]
    elif number[i] > stack[lenStack - 1]:
        if number[i] not in waiting:
            flag = -1
            break
        for j in range(waiting.index(number[i])):
            stack.append(waiting[j])
        ans = ans + '+' * (waiting.index(number[i]) + 1) + '-'
        waiting = waiting[waiting.index(number[i]) + 1:]
    elif number[i] < stack[lenStack - 1]:
        flag = -1
        break
    elif number[i] == stack[lenStack - 1]:
        stack.remove(stack[lenStack - 1])
        ans = ans + '-'

if flag == -1:
    print('NO')
else:
    for i in range(len(ans)):
        print(ans[i])
