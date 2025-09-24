import heapq
def solution(operations):
    answer = []
    nums = []
    heapq.heapify(nums)
    
    for operation in operations:
        op, num = operation.split(" ")
        
        if op == 'I':
            heapq.heappush(nums, int(num))
        elif op == 'D':
            if num == '-1' and nums != []:
                heapq.heappop(nums)
            elif num == '1' and nums != []:
                maxNum = max(nums)
                nums.remove(maxNum)
                
    if nums == []:
        answer = [0, 0]
    else:
        answer.append(max(nums))
        answer.append(heapq.heappop(nums))
    return answer