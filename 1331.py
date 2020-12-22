def main():
    first = []
    final = []
    answer = 1
    visited = [[0 for j in range(6)] for i in range(6)]
    for i in range(36):
        cur = input()
        cur = [int(cur[1]) - 1, ord(cur[0]) - 65]
        if visited[cur[0]][cur[1]] == 1:
            answer = 0
            break
        else:
            visited[cur[0]][cur[1]] = 1
        if i == 0:
            first = cur #최초방문
        if i == 35:
            final = cur #마지막 방문
        if i > 1:
            flag = 0 # last랑 비교해서 가능한 경우
            if abs(last[0] - cur[0]) == 1 and abs(last[1] - cur[1]) == 2:
                flag = 1
            if abs(last[0] - cur[0]) == 2 and abs(last[1] - cur[1]) == 1:
                flag = 1
            if flag == 0:
                answer = 0
                break
        last = cur
    if answer == 1:
        flag = 0 # last랑 비교해서 가능한 경우
        if abs(first[0] - final[0]) == 1 and abs(first[1] - final[1]) == 2:
            flag = 1
        if abs(first[0] - final[0]) == 2 and abs(first[1] - final[1]) == 1:
            flag = 1
        if flag == 0:
            answer = 0
    if answer:
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()
