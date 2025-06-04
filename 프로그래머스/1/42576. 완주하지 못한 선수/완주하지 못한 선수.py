def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for str1, str2 in zip(participant, completion):
        if str1 != str2:
            return str1
    return participant[-1]