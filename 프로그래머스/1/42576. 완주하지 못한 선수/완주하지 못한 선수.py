def solution(participant, completion):
    #participant.sort()
    #completion.sort()
    
    #for str1, str2 in zip(participant, completion):
    #    if str1 != str2:
    #        return str1
    #return participant[-1]
    
    temp = 0
    dic = {}
    
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))
    for c in completion:
        temp -= int(hash(c))
    
    return dic[temp]