def main():
    a = input()
    stack = []
    ans = ''
    for c in a:
        if c == '(':
            stack.append(c)
        elif c == ')':
            for i in range(len(stack) - 1, -1, -1):
                top = stack.pop()
                if top == '(':
                    break
                else:
                    ans += top
        elif c == '+' or c == '-':
            while len(stack) > 0:
                top = stack.pop()
                if top != '(' and top != ')':
                    ans += top
                else:
                    stack.append(top)
                    break
            stack.append(c)
        elif c == '/' or c == '*':
            while len(stack) > 0:
                top = stack.pop()
                if top == '*' or top == '/':
                    ans += top
                else:
                    stack.append(top)
                    break
            stack.append(c)
        else:
            ans += c
    while len(stack) > 0:
        ans += stack.pop()
    print(ans)


if __name__ == '__main__':
    main()
