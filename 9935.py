def main():
    word = list(input())
    bomb = list(input())
    lenB = len(bomb)
    bLast = bomb[-1]
    stack = []
    for i in word:
        stack.append(i)
        if i == bLast and len(stack) >= lenB:
            if stack[len(stack) - lenB:] == bomb:
                for j in range(lenB):
                    stack.pop()
    if len(stack) == 0:
        print('FRULA')
    else:
        for w in stack:
            print(w, end='')


if __name__ == '__main__':
    main()
