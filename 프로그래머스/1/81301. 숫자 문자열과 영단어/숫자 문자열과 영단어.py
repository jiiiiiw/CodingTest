def solution(s):
    result = ""
    tmp = ""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for j in s:
        if(j.isnumeric()):
            result+=j
        else:
            tmp+=j
            if tmp in arr:
                result+=str(arr.index(tmp))
                tmp=""
    return int(result)