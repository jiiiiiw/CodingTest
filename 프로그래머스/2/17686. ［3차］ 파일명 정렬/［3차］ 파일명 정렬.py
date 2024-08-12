def solution(files):
    answer = []
    info = []
    for f in files:
        h, n, f = seperate(f)
        info.append([(h, h.lower()),(n, int(n)),f])
    
    # 비교하는부분 - 비교시에는 소문자로 바꾼값을 기준으로 정렬, 정수값을 기준으로 정렬 (튜플의 1번쨰 원소)
    info = sorted(info, key=lambda x:(x[0][1], x[1][1]))
    print(info)
    
    for i in info:
        temp = ''
        for j in range(len(i)):
            if j!=2:
                temp += i[j][0]
            else:
                temp += i[j]
        answer.append(temp)
            
 
    return answer
 
def seperate(fileName):
    head = getHead(fileName)
    h = len(head)
    number = getNumber(fileName[h:])
    n = len(number)
    tail = fileName[n+h:]
    print(tail)
    return head, number, tail
 
 
 
def getHead(string):
    head = ''
    for s in string:
        if not s.isdigit():
            head += s
        else:
            return head
 
def getNumber(string):
    num = ''
    for s in string:
        if s.isdigit():
            num += s
        else:
            return num
    else:
        return num