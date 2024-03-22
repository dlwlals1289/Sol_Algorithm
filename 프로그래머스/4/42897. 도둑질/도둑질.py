def solution(money):
    answer = 0
    
    dp1 = [0 for _ in range(len(money))] # 첫번째 집 터는 경우
    dp2 = [0 for _ in range(len(money))] # 마지막 집 터는 경우
    
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    dp2[1] = money[1]
    
    n = len(money)
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
        
    max1 = max(dp1)
    max2 = max(dp2)
    answer = max(max1, max2)
    return answer