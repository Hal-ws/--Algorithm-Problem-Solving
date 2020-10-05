import sys


def Main():
    N = int(input())
    order = input()
    lo = len(order)
    value = [0] * N
    for i in range(N):
        value[i] = int(sys.stdin.readline())
    stack = []
    ls = 0
    for i in range(lo):
        flag = 0
        if order[i] == "*":
            temp = stack[ls - 2] * stack[ls - 1]
            flag = 1
        elif order[i] == "+":
            temp = stack[ls - 2] + stack[ls - 1]
            flag = 1
        elif order[i] == "-":
            temp = stack[ls - 2] - stack[ls - 1]
            flag = 1
        elif order[i] == "/":
            temp = stack[ls - 2] / stack[ls - 1]
            flag = 1
        else:
            stack.append(value[ord(order[i]) - 65])
            ls += 1
        if flag:
            del stack[ls - 1]
            del stack[ls - 2]
            ls -= 1
            stack.append(temp)
    ans = stack[0] / 1
    print('%.2f' %ans)


if __name__ == "__main__":
    Main()
