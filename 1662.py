def main():
    S = input()
    stack = []
    cnt = 0
    lastNum = None
    for i in range(len(S)):
        if S[i] != '(' and S[i] != ')':
            cnt += 1
            lastNum = int(S[i])
        else:
            if S[i] == '(':
                stack.append([cnt - 1, lastNum])
                print('stack: %s' %stack)
                cnt = 0
            if S[i] == ')':
                stack.append([cnt, lastNum])
                tmp2 = stack.pop()
                tmp1 = stack.pop()
                stack.append([tmp1[1] * tmp2[0] + tmp1[0], tmp2[1]])
                print('stack: %s' %stack)
                continue
    print(stack)


if __name__ == '__main__':
    main()
