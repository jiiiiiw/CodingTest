def solution(arr):
    sum_list = 0
    for i in range(len(arr)):
        sum_list += arr[i]
    answer = sum_list/len(arr)
    return answer