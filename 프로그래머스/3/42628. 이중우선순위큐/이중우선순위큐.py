from collections import deque
def solution(operations):
    answer = []
    oper = []
    queue = deque()
    
    for i in operations:
        op, num = i.split(" ")
        num = int(num)
        queue = deque(sorted(queue))
        
        if op == "I":
            queue.append(num)
        elif num == 1 and len(queue) > 0:
            queue.pop()
        elif num == -1 and len(queue) > 0:
            queue.popleft()
        else: 
            continue
        # oper.append([op, num])
    
    # for op, num for oper:
    #     if op == "I":

    if len(queue) > 0:
        queue = deque(sorted(queue))
        answer.append(queue.pop())
        answer.append(queue.popleft())
    else:
        answer = [0,0]
            
    return answer