def solution(arr):
    #arr.reverse()
    #answer = []
    
    #answer.append(arr.pop())
    
    #arr.reverse()
    
    #for a in arr:
    #    if a != answer[-1]: answer.append(a)
    
    answer = []
    answer.append(arr[0])
    
    for a in arr:
        if a != answer[-1]: answer.append(a)
    
    return answer