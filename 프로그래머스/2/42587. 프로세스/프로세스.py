from collections import deque

def solution(priorities, location):
    answer = 0
    arr = deque()
    for idx, priority in enumerate(priorities):
        arr.append((priority, idx))

    priorities.sort(reverse = True)
    
    while True:
        priority, idx = arr.popleft()
        
        if idx == location:
            if priority == priorities[answer]:
                break;
            arr.append((priority, idx))
        else :
            if priority == priorities[answer]:
                answer += 1
            else :
                arr.append((priority, idx))
        
    return answer+1