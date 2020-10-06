a = [list(map(int, input().split()))]
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

def printyoot(inputList):
    if sum(inputList) == 3:
        print('A')
    elif sum(inputList) == 2:
        print('B')
    elif sum(inputList) == 1:
        print('C')
    elif sum(inputList) == 0:
        print('D')
    else:
        print('E')

for i in range(3):
    printyoot(a[i])
