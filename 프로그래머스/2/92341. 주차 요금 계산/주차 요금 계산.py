from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    visited = []
    save = defaultdict(int)
    parking = {}
    defaultTime, defaultFee, unitTime, unitFee = fees[0], fees[1], fees[2], fees[3]
    
    for record in records:
        time, carNum, inOut = record.split()
        
        if inOut == 'IN' and carNum not in parking: # 주차된 차가 아니라면
            parking[carNum] = time
        elif inOut == 'OUT' and carNum in parking:
            oHour, oMinute = map(int, time.split(":"))
            iHour, iMinute = map(int, parking[carNum].split(":"))
            total = (oHour - iHour)* 60 + oMinute - iMinute
            
            save[carNum] += total
            parking.pop(carNum)
            
    for carNum, time in parking.items():
        iHour, iMinute = map(int, time.split(":"))
        total = (23 - iHour)* 60 + 59 - iMinute
        
        save[carNum] += total
        
    for carNum, time in sorted(save.items()):
        if time <= defaultTime:
            answer.append(defaultFee)
        else:
            answer.append(defaultFee + math.ceil((time - defaultTime) / unitTime)*unitFee)
    return answer