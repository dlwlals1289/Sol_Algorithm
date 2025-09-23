from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    
    bridge = deque()
    sum = 0
    idx = 0
    
    for i in range(1, bridge_length * n + 2):
        if idx == n and len(bridge) == 0:
            break
            
        for truck, deadline in bridge:
            if deadline == i:
                bridge.popleft()
                sum -= truck
                answer = deadline
                break
                
        if idx != n and sum + truck_weights[idx] <= weight:
            sum += truck_weights[idx]
            bridge.append((truck_weights[idx], i+bridge_length))
            idx += 1
        
    return answer