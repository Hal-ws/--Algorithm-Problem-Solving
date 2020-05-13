import sys
from collections import deque

N = int(sys.stdin.readline())

deque = deque()
length = len(deque)
for i in range(N):
    command = sys.stdin.readline()
    if command == 'pop_front\n':
        if length == 0:
            print(-1)
        else:
            print(deque.popleft())
            length -= 1
    elif command == 'pop_back\n':
        if length == 0:
            print(-1)
        else:
            print(deque.pop())
            length -= 1
    elif command == 'size\n':
        print(length)
    elif command == 'empty\n':
        if length == 0:
            print(1)
        else:
            print(0)
    elif command == 'front\n':
        if length == 0:
            print(-1)
        else:
            print(deque[0])
    elif command == 'back\n':
        if length == 0:
            print(-1)
        else:
            print(deque[length - 1])
    elif command[5] == 'f':
        idx = command.index(' ')
        deque.appendleft(int(command[idx + 1:]))
        length += 1
    else:
        idx = command.index(' ')
        deque.append(int(command[idx + 1:]))
        length += 1
