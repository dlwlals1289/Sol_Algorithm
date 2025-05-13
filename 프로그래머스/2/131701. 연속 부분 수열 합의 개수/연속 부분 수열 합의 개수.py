def solution(elements):
    answer = 0
    arr = []
    n = len(elements)
    memory = []
    
    for i in range(n):
        tmp = sum(elements[:i+1])
        memory.append(tmp)
        
        for j in range(n):
            tmp -= elements[j] 
            tmp += elements[(j+i+1)%n]
            
            memory.append(tmp)
        
        
    answer = len(set(memory))
    return answer