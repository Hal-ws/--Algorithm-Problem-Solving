roomNumber = input()

neededNumberlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while(i < len(roomNumber)):
    neededNumberlist[int(roomNumber[i])] += 1
    i += 1

neededNumberlist[6] += neededNumberlist[9]
neededNumberlist = neededNumberlist[0:9]

if(neededNumberlist[6] % 2 == 0):
    neededNumberlist[6] = neededNumberlist[6] // 2
else:
    neededNumberlist[6] = neededNumberlist[6] // 2 + 1

print(max(neededNumberlist))
