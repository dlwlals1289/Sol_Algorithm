from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    bridge = deque([])
    trucks = deque(truck_weights)
    total_weight = 0
    time = 0
    
    while trucks or bridge:
        time += 1
        while bridge and bridge[0][1] <= time:
            w, t = bridge.popleft()
            total_weight -= w
        if trucks and total_weight + trucks[0] <= weight: #다리 위에 트럭이 더 올라갈 수 있는 경우
            total_weight+=trucks[0]
            bridge.append((trucks[0], time+bridge_length))
            trucks.popleft()
        elif bridge and trucks:
            time = max(time, bridge[0][1] - 1)
    
    return time