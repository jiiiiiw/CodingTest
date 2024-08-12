def solution(records):
    answer = []
    names = {}

    for record in records:
        r = record.split()
        if r[0] == 'Enter':
            answer.append('E'+ r[1])
            names[r[1]] = r[2]
        elif r[0] == 'Leave':
            answer.append('L' + r[1])
        elif r[0] == 'Change':
            names[r[1]] = r[2]
            
    for i in range(len(answer)):
        if answer[i][0] == 'E':
            answer[i] = names[answer[i][1:]] + '님이 들어왔습니다.'
        else:
            answer[i] = names[answer[i][1:]] + '님이 나갔습니다.'
        
    return answer