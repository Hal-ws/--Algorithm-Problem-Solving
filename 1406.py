import sys


def main():
    word = sys.stdin.readline()
    word = word[:len(word) - 1]
    global cursor, length, firstIdx  ## cursor - 1 : linked에서 cursor의 왼쪽에 위치한 문자의 index를 표시.
    cursor, length = len(word), len(word)
    firstIdx = 0 ## linked list에서 처음으로 시작하는 문자의 index
    linked = []
    for i in range(cursor):
        linked.append([i - 1, word[i], i + 1])
    linked[cursor - 1][2] = None
    linked[0][0] = None
    M = int(sys.stdin.readline())
    for i in range(M):
        command = sys.stdin.readline()
        if command[0] == "L":
            movecursor(linked, "L")
        elif command[0] == "D":
            movecursor(linked, "D")
        elif command[0] == "B":
            linked = backSpace(linked)
        else:
            linked = insert(linked, command[2])
    printlinked(linked, firstIdx)

def backSpace(linked):
    global cursor, firstIdx, length
    if cursor > 0:
        if cursor - 1 == firstIdx and linked[cursor - 1][2] != None: ## 처음값인데 끝값은 아닌값 삭제
            linked[linked[cursor - 1][2]][0] = None
            firstIdx = linked[cursor - 1][2] ## 처음 node 삭제하면 두번째 오는 node를 firstIdx로 지정
        elif linked[cursor - 1][0] != None and linked[cursor - 1][2] != None: ## pre node와 next node 지정
            linked[linked[cursor - 1][0]][2] = linked[cursor - 1][2]
            linked[linked[cursor - 1][2]][0] = linked[cursor - 1][0]
        elif linked[cursor - 1][0] != None and linked[cursor - 1][2] == None: ## 마지막 node를 d
            linked[linked[cursor - 1][0]][2] = None
        else: ## 모든 값 삭제함
            firstIdx = None ## 모든 값이 없어졌으니 시작점도 없음
        if linked[cursor - 1][0] != None: ## 첫번째 Node가 아님
            tempcursor = linked[cursor - 1][0] + 1
            linked[cursor - 1][2] = None
            linked[cursor - 1][0] = None ## 현재 Node 의 전후 link 해제
            cursor = tempcursor
        else: ## 첫번째 Node임
            linked[cursor - 1][2] = None
            cursor = 0
        length -= 1
    return linked


def movecursor(linked, direction):
    global cursor, firstIdx
    if direction == "L" and cursor > 0:
        if linked[cursor - 1][0] == None: ## 지금 커서가 가리키는 문자가 첫칸. 커서를 0으로 보낸다.
            cursor = 0
        else:
            cursor = linked[cursor - 1][0] + 1
    if direction == "D":
        if linked[cursor - 1][2] != None:
            cursor = linked[cursor - 1][2] + 1

def insert(linked, add):
    global cursor, firstIdx, length
    if cursor == 0: ## 맨 앞에 삽입할때
        pre = None
        next = firstIdx ## 현재의 firstIdx 가 next값이 된다.
    elif linked[cursor - 1][2] == None: ## 맨 뒤에 삽입할때
        pre = cursor - 1
        next = None
        linked[cursor - 1][2] = cursor
    else:
        pre = cursor - 1
        next = linked[cursor - 1][2]
    linked.append([pre, add, next])
    if cursor == 0:
        firstIdx = len(linked) - 1
    length += 1
    cursor = len(linked)
    if pre == None:
        linked[next][0] = cursor - 1
    elif next == None:
        linked[pre][2] = cursor - 1
    else:
        linked[next][0] = cursor - 1
        linked[pre][2] = cursor - 1
    return linked

def printlinked(linked, firstIdx):
    idx = firstIdx
    if firstIdx != None:
        while linked[idx][2] != None:
            print(linked[idx][1], end='')
            idx = linked[idx][2]
        print(linked[idx][1])

if __name__ == "__main__":
    main()
