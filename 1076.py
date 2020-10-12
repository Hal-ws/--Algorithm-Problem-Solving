rList = [0] * 10
def getR(color):
    if len(color) == 3:
        return 2
    elif len(color) == 4:
        if color[0] == 'b':
            return 6
        else:
            return 8
    elif len(color) == 5:
        if color[2] == 'a':
            return 0
        elif color[2] == 'o':
            return 1
        elif color[2] == 'e':
            return 5
        else:
            return 9
    else:
        if color[0] == 'o':
            return 3
        elif color[0] == 'y':
            return 4
        else:
            return 7

sum = getR(input()) * 10
sum += getR(input())
sum *= pow(10, getR(input()))
print(sum)
