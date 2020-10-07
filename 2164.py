N = int(input())

queue = [0] * N
for i in range(N):
    queue[i] = i + 1

stIdx = 0
endIdx = N - 1
while stIdx < endIdx:
       stIdx += 1
       queue.append(queue[stIdx])
       stIdx += 1
       endIdx += 1

print(queue[stIdx])
