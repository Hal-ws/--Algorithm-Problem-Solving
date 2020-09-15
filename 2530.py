def main():
    A, B, C = map(int, input().split())
    endTime = A * 3600 + B * 60 + C + int(input())
    endTime = endTime % 86400
    hour = endTime // 3600
    endTime = endTime % 3600
    minutes = endTime // 60
    endTime = endTime % 60
    seconds = endTime
    print("%s %s %s" %(hour, minutes, seconds))


if __name__ == "__main__":
    main()
