starttime, startminute = map(int, input().split())
cookingtime = int(input())

endtime = (60 * starttime + startminute + cookingtime) % 1440
print('%s %s' %(endtime // 60, endtime % 60))
