from collections import deque 

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)]) # 다리를 지나고 있는 트럭
    time = 0
    bridge_weight = 0 # 지금 다리위에 있는 트럭들의 무게의 총합
    
    while len(bridge) != 0:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                new = truck_weights.popleft()
                bridge_weight += new
                bridge.append(new)
            else:
                bridge.append(0)
    return time