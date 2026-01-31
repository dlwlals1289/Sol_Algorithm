def solution(sequence):
    answer = 0
    cur1 = cur2 = 0
    max1 = max2 = 0
    
    for i, num in enumerate(sequence):
        s1 = num if i % 2 == 0 else -num
        s2 = num if i % 2 != 0 else -num
        
        cur1 = max(s1, cur1+s1)
        cur2 = max(s2, cur2+s2)
        
        max1 = max(max1, cur1)
        max2 = max(max2, cur2)

    return max(max1, max2)