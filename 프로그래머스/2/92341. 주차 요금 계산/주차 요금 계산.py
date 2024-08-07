import math # ceil - 올림 함수를 가져오기 위해서

def solution(fees, records):
    time = dict() # 차량번호 : 시간리스트
    stay = dict() # 차량번호 : 머문 누적 시간
    pay = []
    
    '''
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    '''
    
    """
    [180, 5000, 10, 600]
    """
    
    for data in records:
        car_num = data[6:10]
        h = int(data[0:2])
        m = int(data[3:5])
        
        if car_num in time:
            time[car_num] += [h*60 + m] # 누적분을 리스트에 추가시킨다
        else:
            time[car_num] = [h*60 + m]
            stay[car_num] = 0 # 머문 시간을 초기화 해주는 작업
            
    for car_num in time:
        if len(time[car_num]) % 2 != 0:
            time[car_num].append(23*60 + 59) # 아웃 기록이 없으면 23:59에 나간걸로 처리
            
        for i in range(len(time[car_num]) // 2): # 짝을 지었으니 반만 걸러도 ㄱㅊ
            inner = time[car_num][i*2]
            outer = time[car_num][i*2+1]
            stay[car_num] += outer - inner
            
    for car in sorted(stay):
        standard = fees[0]
        
        if stay[car] <= standard:
            pay.append(fees[1])
        else:
            pay.append(fees[1] + int(math.ceil((stay[car] - standard) / fees[2]) * fees[3])) # 실수 조심
            
    return pay