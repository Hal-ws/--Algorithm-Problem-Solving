import sys

N = int(sys.stdin.readline())

queue = []
stIdx = 0
endIdx = -1
for i in range(N):
    command = sys.stdin.readline()
    if command == 'pop\n':
        if stIdx > endIdx:
            print(-1)
        else:
            print(queue[stIdx])
            stIdx += 1
    elif command == 'size\n':
        print(endIdx - stIdx + 1)
    elif command == 'empty\n':
        if stIdx > endIdx:
            print(1)
        else:
            print(0)
    elif command == 'front\n':
        if stIdx > endIdx:
            print(-1)
        else:
            print(queue[stIdx])
    elif command == 'back\n':
        if stIdx > endIdx:
            print(-1)
        else:
            print(queue[endIdx])
    else:
        a, b = map(str, command.split())
        queue.append(b)
        endIdx += 1
