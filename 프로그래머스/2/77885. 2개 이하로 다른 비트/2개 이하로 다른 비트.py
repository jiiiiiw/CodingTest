#1) 짝수의 경우
#가장 뒤에 있는 0을 1로

#2) 홀수의 경우
#가장 마지막의 0을 기준으로 그리고 그 다음 값에 대한 값을 1, 0 으로

def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:  # 짝수일 경우
            answer.append(n + 1)
        else:  # 홀수 인 경우
            temp = '0' + bin(n)[2:]
            right_idx = temp.rfind('0')
            temp_list = list(temp)
            
            temp_list[right_idx] = '1'
            temp_list[right_idx+1] = '0'
            
            temp_str = "".join(temp_list)
            
            answer.append(int(temp_str, 2))
                
    return answer