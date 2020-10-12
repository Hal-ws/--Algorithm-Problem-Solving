import sys

K = int(sys.stdin.readline())

stack = []
for i in range(K):
    command = int(sys.stdin.readline())
    if command == 0:
        del stack[len(stack) - 1]
    else:
        stack.append(command)
print(sum(stack))
