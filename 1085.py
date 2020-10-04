x, y, w, h= map(int, input().split(' '))

if(w - x < x):
    xValue = w - x
else:
    xValue = x
if(h - y < y):
    yValue = h - y
else:
    yValue = y

if(xValue < yValue):
    print(xValue)
else:
    print(yValue)
