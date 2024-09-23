def solution(diffs, times, limit):
    n = len(diffs)
    
    # 주어진 숙련도 level에서 퍼즐을 풀 때 걸리는 총 시간을 계산하는 함수
    def calc_total_time(level):
        total_time = times[0]  # 첫 번째 퍼즐은 무조건 풀 수 있음
        for i in range(1, n):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1]
            
            if diff <= level:
                # 숙련도가 충분해서 바로 풀 수 있는 경우
                total_time += time_cur
            else:
                # 숙련도가 부족하여 퍼즐을 여러 번 틀리는 경우
                fails = diff - level
                total_time += fails * (time_cur + time_prev) + time_cur
                
            # 제한 시간을 초과하는 경우
            if total_time > limit:
                return total_time
        
        return total_time
    
    # 이진 탐색을 통해 최소 숙련도를 찾음
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if calc_total_time(mid) <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer