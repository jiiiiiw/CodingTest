def solution(citations):
    citations.sort(reverse = True)
    Hindex = 0
    
    for idx in range(len(citations)):
        MinVal = idx + 1
        CurrVal = citations[idx]
        if MinVal <= CurrVal:
            Hindex = MinVal
        else:
            break
    return Hindex