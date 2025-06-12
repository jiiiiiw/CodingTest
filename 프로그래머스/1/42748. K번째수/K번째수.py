def solution(array, commands):
    answer = []
    
    for c in commands:
        new_array = array[c[0]-1:c[1]]
        new_array.sort()
        print(new_array)
        answer.append(new_array[c[2]-1])
    
    return answer