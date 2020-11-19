def main():
    command = list(map(str, input().split()))
    header = command[0]
    for i in range(1, len(command)):
        print('%s%s %s;' %(header, bodytail(command[i])[0], bodytail(command[i])[1]))


def bodytail(a):
    body = ''
    tail = ''
    reverseflag = 0 # 변수의 오른쪽에 있는 변수형일때는 0, 아닐때는 1
    for i in range(len(a) - 1, -1, -1):
        if reverseflag == 0:
            if a[i] != ';' and a[i] != ',' and a[i] != '[':
                if a[i] == '&' or a[i] == '*':
                    body += a[i]
                elif a[i] == ']':
                    body += '[]'
                else:
                    tail += a[i]
                    reverseflag = 1
        else:
            tail = a[i] + tail


    return [body, tail]


if __name__ == "__main__":
    main()
