broken = int(input())
using = int(input())

if using == 0:
    print(broken - 1)
elif broken == 1:
    print(using * 8)
elif broken == 2:
    print(4 * (using + 1) - 1 - pow(-1, using) - 1)
elif broken == 3:
    print(using * 4 + 2)
elif broken == 4:
    print(4 * (using + 1) - 1 + pow(-1, using) - 1)
else:
    print(using * 8 + 4)
