import sys

T = int(sys.stdin.readline())


for i in range(T):
    flag = 0
    check = sys.stdin.readline()
    stack = []
    for j in range(len(check) - 1):
        if check[j] == '(':
            stack.append(check[j])
        elif check[j] == ')' and '(' not in stack:
            flag = -1
            break
        else:
            stack.pop()
    if flag == -1 or len(stack) != 0:
        print('NO')
    else:
        print('YES')
