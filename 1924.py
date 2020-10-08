x, y= map(int, input().split(' '))

if(x == 1):
    dayDifference =  y - 1
elif(x == 2):
    dayDifference = 30 + y
elif(x == 3):
    dayDifference = 58 + y
elif(x == 4):
    dayDifference = 89 + y
elif(x == 5):
    dayDifference = 119 + y
elif(x == 6):
    dayDifference = 150 + y
elif(x == 7):
    dayDifference = 180 + y
elif(x == 8):
    dayDifference = 211 + y
elif(x == 9):
    dayDifference = 242 + y
elif(x == 10):
    dayDifference = 272 + y
elif(x == 11):
    dayDifference = 303 + y
else:
    dayDifference = 333 + y

if(dayDifference % 7 == 0):
    print("MON")
elif(dayDifference % 7 == 1):
    print("TUE")
elif(dayDifference % 7 == 2):
    print("WED")
elif(dayDifference % 7 == 3):
    print("THU")
elif(dayDifference % 7 == 4):
    print("FRI")
elif(dayDifference % 7 == 5):
    print("SAT")
else:
    print("SUN")
