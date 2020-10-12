import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    command = sys.stdin.readline()
    if len(command) > 6:
        idx = command.index(' ')
        stack.append(int(command[idx + 1:]))
    elif command[0] == 'p':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
            del stack[len(stack) - 1]
    elif command[0] == 's':
        print(len(stack))
    elif command[0] == 'e':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
