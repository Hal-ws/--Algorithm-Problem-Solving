inputVal = input()

sign = []
numbers = []
i = 0
marker = -1
flag = 0
while i < len(inputVal):
    if inputVal[i] == '+' or inputVal[i] == '-':
        sign.append(inputVal[i])
        if i == 0:
            marker = 0
        if i != 0:
            numbers.append(int(inputVal[marker + 1:i]))
            marker = i
    if i == len(inputVal) - 1:
        numbers.append(int(inputVal[marker + 1:i + 1]))
    i += 1

for i in range(len(sign)):
    if(sign[i] == '-'):
        flag = 1
        break
if flag == 0:
    print(sum(numbers))
elif len(sign) == len(numbers):
    print(-sum(numbers[:len(numbers)]))
else:
    print(sum(numbers[0:i + 1]) - sum(numbers[i + 1:len(numbers)]))
