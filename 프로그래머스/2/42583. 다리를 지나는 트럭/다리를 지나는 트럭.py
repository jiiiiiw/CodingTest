#from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    flag = 0
    current_truck = [0] * bridge_length
    current_weight = sum(current_truck)
    
    while flag < len(truck_weights):
        p = current_truck.pop(0)
        current_weight -= p
        if current_weight + truck_weights[flag] > weight:
            current_truck.append(0)
            answer += 1
        else:
            if flag == len(truck_weights) - 1:
                answer += (bridge_length + 1)
            else:
                current_truck.append(truck_weights[flag])
                current_weight += truck_weights[flag]
                answer += 1
                
            flag += 1
    
    return answer