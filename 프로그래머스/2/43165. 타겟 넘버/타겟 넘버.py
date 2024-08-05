def dfs(numbers, target_num, curr_sum, curr_idx):
    if curr_idx == len(numbers):
        # 타케트가 만들어지는 경우
        if curr_sum == target_num:
            return 1
        else:
            return 0
    else:
        answer = 0
        answer += dfs(numbers, target_num, curr_sum+numbers[curr_idx], curr_idx+1)
        answer += dfs(numbers, target_num, curr_sum-numbers[curr_idx], curr_idx+1)
        return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer