
def solution(N, number):    
    dp = dict()
    done = set()
    
    dp[1] = set([N])
    if number == N:
        return 1
    
    tmp = N
    for i in range(2, 9):
        dp[i] = set()
        
        tmp  = (tmp*10) + N
        
        if tmp == number:
            return i
        dp[i].add(tmp)
        done.add(tmp)

    for i in range(2, 9):
        idx = (i//2)

        for j in range(1, idx + 1):
            prev1 = dp[j]
            prev2 = dp[i-j]
            
            for val1 in prev1:
                for val2 in prev2:
                    for k in range(6):
                        tmp = 0
                        if k == 0:
                            tmp = val1 + val2
                        elif k == 1:
                            tmp = val1 - val2
                        elif k == 2:
                            tmp = val1 * val2
                        elif k == 3:
                            tmp = val1 // val2
                        elif k == 4:
                            tmp = val2 - val1
                        elif k == 5:
                            tmp = val2 // val1

                
                        if tmp == number:
                            return i
                        elif tmp not in done and tmp != 0:
                            dp[i].add(tmp)
                            done.add(tmp)
    return -1